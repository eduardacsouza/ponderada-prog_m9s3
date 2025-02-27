from .server_selector import get_best_server
from .streaming_repository import log_streaming

def start_streaming(user_id: int, content_id: str) -> str:
    """
    Inicia o streaming de um conteúdo, escolhendo o melhor servidor disponível.
    Implementa fallback para garantir resiliência do sistema.
    """
    if not user_id or not content_id:
        raise ValueError("Usuário e conteúdo são obrigatórios.")
    
    server_url = get_best_server()
    
    success = log_streaming(user_id, content_id, server_url)
    if not success:
        raise ValueError("Falha ao registrar streaming.")
    
    return server_url