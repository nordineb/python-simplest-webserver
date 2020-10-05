import http.server
import socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')

httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
