import pytest
from ..src.services.server_selector import select_best_server

# Teste para selecionar o melhor servidor baseado na carga e latência
def test_select_best_server():
    servers = [
        {"id": 1, "load": 30, "latency": 100},
        {"id": 2, "load": 20, "latency": 150},
        {"id": 3, "load": 10, "latency": 200},
    ]
    best_server = select_best_server(servers)
    assert best_server == {"id": 3, "load": 10, "latency": 200}

# Teste para lidar com uma lista vazia de servidores
def test_select_best_server_empty_list():
    servers = []
    best_server = select_best_server(servers)
    assert best_server is None

# Teste para quando todos os servidores estão sobrecarregados
def test_select_best_server_high_load():
    servers = [
        {"id": 1, "load": 95, "latency": 100},
        {"id": 2, "load": 97, "latency": 120},
        {"id": 3, "load": 99, "latency": 150},
    ]
    best_server = select
