database_streaming_logs = []

def log_streaming(user_id: int, content_id: str, server: str) -> bool:
    """
    Registra o evento de streaming no banco de dados fictício.
    """
    try:
        log = {
            "user_id": user_id,
            "content_id": content_id,
            "server": server
        }
        database_streaming_logs.append(log)
        return True
    except Exception as e:
        print(f"Erro ao registrar streaming: {e}")
        return False

def get_streaming_logs():
    """
    Retorna todos os logs de streaming registrados.
    """
    return database_streaming_logs