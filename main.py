from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uuid

app = FastAPI()

# Simulación de almacenamiento en memoria para tokens generados
tokens_db = {}

# Modelo de datos para solicitudes
class PuntoRecoleccion(BaseModel):
    id_punto: str

# Endpoint para generar un token de sorteo
@app.post("/generate-token")
async def generate_token(punto: PuntoRecoleccion):
    id_punto = punto.id_punto
    # Validación simple para ID vacío
    if not id_punto.strip():
        raise HTTPException(status_code=400, detail="El ID del punto no puede estar vacío.")
    
    # Generación del token único
    token = f"{id_punto}-{uuid.uuid4()}-{datetime.utcnow().isoformat()}"
    # Almacenar el token generado
    tokens_db[id_punto] = tokens_db.get(id_punto, []) + [token]
    return {"token": token}

# Endpoint para listar tokens generados por un punto de recolección
@app.get("/tokens/{id_punto}")
async def get_tokens(id_punto: str):
    if id_punto not in tokens_db:
        raise HTTPException(status_code=404, detail="No se encontraron tokens para este punto de recolección.")
    return {"id_punto": id_punto, "tokens": tokens_db[id_punto]}
