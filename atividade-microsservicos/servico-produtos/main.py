from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/produtos/{id}")
async def get_produto(id: int):
    return {"id": id, "nome": "Teclado Mecânico", "preco": 250.0}