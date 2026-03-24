from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/estoque/{id}")
async def consultar_estoque(id: int):
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            # "produtos" é o nome do serviço no docker-compose
            response = await client.get(f"http://produtos:8001/produtos/{id}")
            response.raise_for_status()
            dados_produto = response.json()
            
        return {
            "produto_id": id,
            "quantidade_em_estoque": 15,
            "detalhes": dados_produto
        }
    except httpx.HTTPStatusError:
        raise HTTPException(status_code=404, detail="Produto não encontrado no catálogo")
    except httpx.ConnectError:
        raise HTTPException(status_code=503, detail="Serviço de Catálogo fora do ar")
    except httpx.ReadTimeout:
        raise HTTPException(status_code=504, detail="O Serviço de Catálogo demorou demais para responder")