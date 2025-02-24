import random

SERVERS = [
    "https://server1.netflix.com",
    "https://server2.netflix.com",
    "https://backup.netflix.com"
]

UNAVAILABLE_SERVERS = {"https://server1.netflix.com"}  # Simulando indisponibilidade

def get_best_server() -> str:
    """
    Seleciona o melhor servidor disponível para streaming.
    Utiliza fallback em caso de indisponibilidade.
    """
    for server in SERVERS:
        if server not in UNAVAILABLE_SERVERS:
            return server
    return "https://fallback.netflix.com"  # Fallback final