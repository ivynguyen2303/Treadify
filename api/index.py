from http.server import BaseHTTPRequestHandler #imported to have an http endpoint
import json

# pylint: disable-all

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write({'gfd': 'gfgfd'}.encode())