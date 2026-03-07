from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

PORT = 8080

class Handler(SimpleHTTPRequestHandler):

    def do_POST(self):

        if self.path == "/login":

            length = int(self.headers.get("Content-Length"))
            data = self.rfile.read(length)

            body = json.loads(data)

            gmail = body["gmail"]
            password = body["password"]

            with open("../database/users.json") as f:
                users = json.load(f)

            for u in users:

                if u["gmail"] == gmail and u["password"] == password:

                    with open("../database/sessions.json") as f:
                        sessions = json.load(f)

                    sessions.append({"gmail":gmail})

                    with open("../database/sessions.json","w") as f:
                        json.dump(sessions,f)

                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"ok")
                    return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"error")

        else:

            super().do_POST()

print("Servidor activo en puerto",PORT)

HTTPServer(("0.0.0.0",PORT),Handler).serve_forever()