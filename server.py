from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8000

folder = input("Enter folder to serve (default = current): ").strip()

if folder:
    if not os.path.isdir(folder):
        print("Invalid folder path")
        exit()
    os.chdir(folder)

handler = SimpleHTTPRequestHandler
server = HTTPServer(("localhost", PORT), handler)

print(f"Serving at http://localhost:{PORT}")
print("Press Ctrl+C to stop")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped")
