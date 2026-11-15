/* ============================================================================
   The card in real 3D (WebGL / three.js).

   Physics stay where they were: app.js owns the springs, the drag, the
   momentum and the snapping, and calls window.__cardGL.render(ry, rx) every
   frame. This file only turns those two angles into a lit, solid object.
   If WebGL is missing or anything here fails, nothing changes — the CSS card
   underneath keeps working as before.

   The geometry is the real thing: 54 × 85.6 × 0.76 mm, 3.18 mm corners
   (ISO/IEC 7810 ID-1), white side and black side printed edge to edge.
   ========================================================================= */
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.165.0/+esm';
import { RoomEnvironment } from 'https://cdn.jsdelivr.net/npm/three@0.165.0/examples/jsm/environments/RoomEnvironment.js/+esm';

export { THREE };

// Centimetres. Proportions are what matter; the camera does the rest.
export const CARD = { w: 5.4, h: 8.56, d: 0.076, r: 0.318 };

function roundedRect(w, h, r) {
  const s = new THREE.Shape();
  const x = -w / 2, y = -h / 2;
  s.moveTo(x + r, y);
  s.lineTo(x + w - r, y);
  s.quadraticCurveTo(x + w, y, x + w, y + r);
  s.lineTo(x + w, y + h - r);
  s.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  s.lineTo(x + r, y + h);
  s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r);
  s.quadraticCurveTo(x, y, x + r, y);
  return s;
}

/** A face plane whose UVs run 0→1 across the whole card, so the printed
 *  artwork lands exactly where it does on the physical card. */
function faceGeometry(shape) {
  const g = new THREE.ShapeGeometry(shape, 24);
  const pos = g.attributes.position, uv = g.attributes.uv;
  for (let i = 0; i < pos.count; i++) {
    uv.setXY(i, (pos.getX(i) + CARD.w / 2) / CARD.w, (pos.getY(i) + CARD.h / 2) / CARD.h);
  }
  uv.needsUpdate = true;
  return g;
}

export function loadTextures(renderer, base) {
  const loader = new THREE.TextureLoader();
  const aniso = renderer.capabilities.getMaxAnisotropy();
  const one = url => new Promise((res, rej) => loader.load(url, t => {
    t.colorSpace = THREE.SRGBColorSpace;
    t.anisotropy = aniso;
    res(t);
  }, undefined, rej));
  return Promise.all([one(base + 'assets/img/tex-front.png?v=1'), one(base + 'assets/img/tex-back.png?v=1')]);
}

/** One card: white side facing +z, black side facing −z. */
export function makeCard(front, back) {
  const shape = roundedRect(CARD.w, CARD.h, CARD.r);
  const group = new THREE.Group();

  // The PVC body. Its own caps sit just under the printed faces.
  const body = new THREE.Mesh(
    new THREE.ExtrudeGeometry(shape, { depth: CARD.d, bevelEnabled: false, curveSegments: 24 }),
    new THREE.MeshStandardMaterial({ color: 0xE4E4E0, roughness: 0.45 }),
  );
  body.geometry.translate(0, 0, -CARD.d / 2);
  body.castShadow = true;
  body.receiveShadow = true;
  group.add(body);

  const fg = faceGeometry(shape);
  const eps = 0.0006;

  // Matte print. The black side is slightly less rough, as real matte black
  // laminate is — that's what gives it the soft sheen in the photos.
  const frontMesh = new THREE.Mesh(fg, new THREE.MeshPhysicalMaterial({
    map: front, roughness: 0.7, metalness: 0,
  }));
  frontMesh.position.z = CARD.d / 2 + eps;
  frontMesh.receiveShadow = true;

  const backMesh = new THREE.Mesh(fg, new THREE.MeshPhysicalMaterial({
    map: back, roughness: 0.58, metalness: 0, clearcoat: 0.06, clearcoatRoughness: 0.5,
  }));
  backMesh.rotation.y = Math.PI;
  backMesh.position.z = -(CARD.d / 2 + eps);
  backMesh.receiveShadow = true;

  group.add(frontMesh, backMesh);
  return group;
}

export function makeRenderer(canvas, opts = {}) {
  const renderer = new THREE.WebGLRenderer({
    canvas, antialias: true, alpha: true, preserveDrawingBuffer: !!opts.preserve,
  });
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.NeutralToneMapping;   // keeps Google's colours true
  renderer.toneMappingExposure = 1.0;
  renderer.setClearColor(0x000000, 0);
  return renderer;
}

/** Studio light: a soft room for reflections plus one key light from the
 *  upper left, fixed in the world so highlights travel as the card turns. */
export function makeScene(renderer, { envIntensity = 0.5, key = 0.9 } = {}) {
  const scene = new THREE.Scene();
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = envIntensity;

  const keyLight = new THREE.DirectionalLight(0xffffff, key);
  keyLight.position.set(-4, 6, 8);
  scene.add(keyLight);
  return { scene, keyLight };
}

/* ---------------------------------------------------------------- viewer */
async function mountViewer() {
  const wrap = document.querySelector('[data-card3d]');
  if (!wrap || wrap.dataset.gl) return;

  const canvas = document.createElement('canvas');
  canvas.className = 'card3d__gl';
  canvas.setAttribute('aria-hidden', 'true');

  let renderer;
  try {
    renderer = makeRenderer(canvas);
  } catch (_) { return; }          // no WebGL: the CSS card stays

  const base = new URL('..', import.meta.url).href;
  const [front, back] = await loadTextures(renderer, base);
  const { scene } = makeScene(renderer);
  const card = makeCard(front, back);
  scene.add(card);

  // The canvas is 1.6× the wrapper on every axis so a tilted card never
  // clips. The camera frames the card at rest to exactly the wrapper's box.
  const PAD = 1.6;
  const camera = new THREE.PerspectiveCamera(30, 1, 1, 100);
  const dist = (PAD * CARD.h) / (2 * Math.tan(THREE.MathUtils.degToRad(15)));
  camera.position.set(0, 0, dist);
  camera.lookAt(0, 0, 0);

  let visible = true, last = null;
  const resize = () => {
    const r = wrap.getBoundingClientRect();
    if (!r.width) return;
    renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
    renderer.setSize(r.width * PAD, r.height * PAD, false);
    camera.aspect = r.width / r.height;
    camera.updateProjectionMatrix();
    last = null;
  };
  new ResizeObserver(resize).observe(wrap);
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(wrap);

  wrap.appendChild(canvas);
  resize();

  window.__cardGL = {
    render(ry, rx) {
      if (!visible) return;
      const key = ry.toFixed(2) + ':' + rx.toFixed(2);
      if (key === last) return;
      last = key;
      // CSS rotateX(+) tips the top away; three's +x tips it toward us.
      card.rotation.set(THREE.MathUtils.degToRad(-rx), THREE.MathUtils.degToRad(ry), 0, 'XYZ');
      renderer.render(scene, camera);
    },
  };
  wrap.dataset.gl = 'true';
}

if (!window.__cardNoViewer) {
  mountViewer().catch(err => console.warn('card3d: falling back to CSS card', err));
}
