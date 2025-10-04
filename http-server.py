from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0" # 127.0.0.1 for local development
PORT = 8000

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            response = {"message": "Hello, world!"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        elif self.path == "/status":
            self._set_headers()
            response = {"status": "ok"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self._set_headers(404)
            response = {"error": "Not found"}
            self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            data = {}

        self._set_headers()
        response = {"received": data}
        self.wfile.write(json.dumps(response).encode("utf-8"))

def run():
    server = HTTPServer((HOST, PORT), SimpleAPIHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
