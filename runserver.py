import BaseHTTPServer
import CGIHTTPServer

BaseHTTPServer.HTTPServer(( '127.0.0.1', 8000 ), CGIHTTPServer.CGIHTTPRequestHandler ).serve_forever()

