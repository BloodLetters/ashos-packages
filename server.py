import http.server
import socketserver
import os
import sys
import socket
import json

DEFAULT_PORT = 8000

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class PackageRepositoryHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def log_message(self, format, *args):
        sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")
        sys.stdout.flush()

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.join(base_dir, "package")

    if not os.path.isdir(package_dir):
        if os.path.exists(os.path.join(base_dir, "packages.json")):
            package_dir = base_dir
        else:
            print(f"Error: package directory not found at {package_dir}")
            sys.exit(1)

    os.chdir(package_dir)

    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    local_ip = get_local_ip()

    print("=" * 65)
    print(" AshOS Local Package Repository Server")
    print("=" * 65)
    print(f" Serving Directory : {package_dir}")
    print(f" Localhost URL     : http://127.0.0.1:{port}")
    print(f" LAN IP URL        : http://{local_ip}:{port}")
    print(f" Wokwi / QEMU URL  : http://10.0.2.2:{port}")
    print("=" * 65)
    print(" In AshOS shell, configure repository by running:")
    print(f"   ash repo http://{local_ip}:{port}     (for real hardware)")
    print(f"   ash repo http://10.0.2.2:{port}       (for Wokwi simulation)")
    print(" Then run:")
    print("   ash update")
    print("   ash install <package_name>")
    print("=" * 65)
    print(f" Listening on port {port} (Press Ctrl+C to stop)...")
    print()

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), PackageRepositoryHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    main()
