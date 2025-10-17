from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {"name": "sam Larry", "Tarck": "AI Developer"},
    {"name": "Reubem stone", "Tarck": "AI Developer"},
    {"name": "John Cena", "Tarck": "AI Developer"}
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_DELETE(self):
        content_size = int(self.headers.get("Content-Length", 0))
        parsed_data = self.rfile.read(content_size)
        delete_data = json.loads(parsed_data)

        name_to_delete = delete_data.get("name")
        if not name_to_delete:
            self.send_data({"Error": "Missing 'name' in request body"}, status=400)
            return

        for item in data:
            if item.get("name") == name_to_delete:
                data.remove(item)
                self.send_data({
                    "Message": f"Record with name '{name_to_delete}' deleted",
                    "Remaining Data": data
                })
                return

        self.send_data({"Error": f"No record found for name '{name_to_delete}'"}, status=404)

def run():
    HTTPServer(('localhost', 8000), BasicAPI).serve_forever()

print("Application is running ")
run()
