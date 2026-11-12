from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, {"status": "ok", "service": "qookie"})
        elif self.path == "/":
            self._send(200, {"message": "qookie backend"})
        else:
            self._send(404, {"error": "not found"})


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 9000), Handler)
    print("qookie running on http://localhost:9000")
    server.serve_forever()
