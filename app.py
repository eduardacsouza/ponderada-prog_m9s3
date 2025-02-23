from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.services.streaming import start_streaming

app = FastAPI()

class StreamingRequest(BaseModel):
    user_id: int
    content_id: str

@app.post("/stream/")
def stream_content(request: StreamingRequest):
    """
    Endpoint para iniciar a reprodução de um conteúdo na Netflix.
    Se o servidor primário estiver indisponível, utiliza fallback automático.
    """
    try:
        server_url = start_streaming(request.user_id, request.content_id)
        return {"message": "Streaming iniciado", "server": server_url}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
