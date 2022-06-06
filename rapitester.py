#!/usr/bin/python3
import ssl, http.server

httpd = http.server.HTTPServer(('0.0.0.0', 9000), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="/etc/rapitestertls/tls.key", certfile='/etc/rapitestertls/tls.crt', server_side=True)
httpd.serve_forever()