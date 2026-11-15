#!/usr/bin/env python3
"""Lokal server der efterligner Vercels cleanUrls: /faq -> faq.html, /guides -> guides/index.html.

    python3 tools/serve.py [port]
"""
import http.server, os, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4176


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def translate_path(self, path):
        full = super().translate_path(path)
        if not path.split("?")[0].endswith("/"):
            if os.path.isfile(full + ".html"):
                return full + ".html"
            if os.path.isdir(full) and os.path.isfile(os.path.join(full, "index.html")):
                return os.path.join(full, "index.html")
        return full

    def send_error(self, code, message=None, explain=None):
        if code == 404 and (ROOT / "404.html").exists():
            self.error_message_format = (ROOT / "404.html").read_text(encoding="utf-8")
        super().send_error(code, message, explain)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


http.server.ThreadingHTTPServer(("", PORT), Handler).serve_forever()
