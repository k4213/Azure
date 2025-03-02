import http.server
import ssl

port = 6006
server_address = ('0.0.0.0', port)

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(server_address, handler)


httpd.socket = ssl.wrap_socket(httpd.socket, 
                               certfile="cert.pem", 
                               keyfile="key.pem", 
                               server_side=True)

print(f"Serving HTTPS on 0.0.0.0 port {port}...")
httpd.serve_forever()