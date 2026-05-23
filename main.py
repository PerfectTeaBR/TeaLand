from fastapi import FastAPI
from models import *
from datetime import datetime, timezone
import uvicorn
import json
import os

app = FastAPI()

@app.get("/") # A Simple little test...
async def root():
    return {"message": "A TeaLand está online e operante!"}

# ===[ Post Models ]===

# NOTE: Esses modelos são apenas para LuaBot!!

@app.post("/api/model/users")
async def post_user_model(model: UserModel):
    return model

@app.post("/api/model/server")
async def post_server_model(model: ServerModel):
    return model

dirname = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.normpath(os.path.join(
    dirname, "tealand.json"
))

def create_config():
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            tealand_raw = json.load(f)
            modelo_json = {
                "name": "TeaLand Config v1",
                "criado_em": datetime.now(timezone.utc).isoformat()
            }
            
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(modelo_json, f, indent=4, ensure_ascii=False)
        print("Modelo criado!")

    except FileNotFoundError:
        print("Arquivo não encontrado.")

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
