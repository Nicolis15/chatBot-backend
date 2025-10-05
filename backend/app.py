# backend.py
from fastapi import FastAPI

app = FastAPI()  # 👈 ESTA LÍNEA ES LA CLAVE

@app.get("/")
def home():
    return {"message": "Servidor activo 🚀"}
