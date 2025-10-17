from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "name": "sam larry",
        "track": "AI developer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=201):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_PATCH(self):
        content_size = int(self.headers.get("Content-Length", 0))
        parsed_data = self.rfile.read(content_size)
        parsed_data = json.loads(parsed_data)

        if data:
            data[0].update(parsed_data)
            self.send_data({
                "message": "Data Edited",
                "data": data[0]
            }, status=201)
        else:
            self.send_data({
                "message": "No data is patch"
            }, status=400)

def run():
    print("Application is Running..")
    HTTPServer(('0.0.0.0', 8000), BasicAPI).serve_forever()

run()
