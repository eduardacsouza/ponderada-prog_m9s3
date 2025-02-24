import pytest
import time
from ..src.services.server_selector import select_best_server

# Teste para validar tempo máximo de failover (100 ms)
def test_failover_time():
    servers = [
        {"id": 1, "load": 30, "latency": 100},
        {"id": 2, "load": 20, "latency": 150},
        {"id": 3, "load": 10, "latency": 200},
    ]
    
    start_time = time.time()
    best_server = select_best_server(servers)
    elapsed_time = (time.time() - start_time) * 1000  # Converter para ms

    assert best_server is not None, "Nenhum servidor foi selecionado"
    assert elapsed_time <= 100, f"Tempo de failover excedeu o limite: {elapsed_time:.2f} ms"
