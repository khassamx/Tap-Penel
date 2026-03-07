import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

# ---- Config ----
PORT = 8080
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # Carpeta donde está server.py
DATABASE_DIR = os.path.join(ROOT_DIR, "database")       # Carpeta database
USERS_FILE = os.path.join(DATABASE_DIR, "users.json")
SESSIONS_FILE = os.path.join(DATABASE_DIR, "sessions.json")

# Asegurar que exista carpeta database
os.makedirs(DATABASE_DIR, exist_ok=True)

# Inicializar archivos si no existen
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump([{"gmail":"admin@gmail.com","password":"123456"}], f)

if not os.path.exists(SESSIONS_FILE):
    with open(SESSIONS_FILE, "w") as f:
        json.dump([], f)

# Cambiar directorio para servir archivos web
os.chdir(ROOT_DIR)

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/login":
            length = int(self.headers.get("Content-Length"))
            data = self.rfile.read(length)
            body = json.loads(data)

            gmail = body.get("gmail")
            password = body.get("password")

            with open(USERS_FILE) as f:
                users = json.load(f)

            # Validar login
            valid_user = next((u for u in users if u["gmail"] == gmail and u["password"] == password), None)

            if valid_user:
                # Guardar sesión
                with open(SESSIONS_FILE, "r") as f:
                    sessions = json.load(f)
                if not any(s["gmail"] == gmail for s in sessions):
                    sessions.append({"gmail": gmail})
                    with open(SESSIONS_FILE, "w") as f:
                        json.dump(sessions, f)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"ok")
            else:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"error")
        else:
            super().do_POST()

# ---- Iniciar servidor ----
print(f"Servidor activo en puerto {PORT} 🚀")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()