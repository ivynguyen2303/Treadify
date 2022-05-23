from http.server import BaseHTTPRequestHandler #imported to have an http endpoint
import json

# pylint: disable-all

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        self.process_response (
            status_code = 200,
            header = ('Content-Type', 'application/json'),
            data = json.dumps({'pp': 'chicken'}, ensure_ascii = False, indent = 4)

        )