# ponderada-prog_m9s3

Este repositório contém a entrega da atividade ponderada da semana 3:

Selecione uma empresa digital e descreva como algum aspecto não funcional da sua arquitetura é sustentada por códigos que suportam a operação:
1) Documentar os requisitos em código (1 RF - 5.0 pontos);  
2) Aferir a qualidade dos requisitos envolvidos no sistema, ao executar estes códigos (1 RNF - 5.0 pontos).  

---

Empresa Selecionada: **Netflix**  

A **Netflix** é uma das maiores plataformas de streaming do mundo e precisa garantir a disponibilidade e escalabilidade do seu sistema, mesmo sob alta demanda. Um aspecto não funcional fundamental para sua operação é a Resiliência, que impede que falhas de servidores ou sobrecargas afetem a experiência do usuário.

### 1) Requisito Funcional (RF)  
**RF Selecionado:** **Disponibilidade de servidores para que o usuário assista conteúdos.**  

**Descrição:**  
A plataforma deve permitir que os usuários assistam a conteúdos sob demanda sem interrupções.  

**Implementação no Código:**

[`server_selector.py`](./src/services/server_selector.py)<br>
Neste código, os servidores disponíveis são monitorados e ordenados com base na latência.  
Se um servidor falhar, o sistema escolhe o próximo melhor servidor para garantir que o usuário continue assistindo sem interrupções. 

[`streaming.py`](./src/services/streaming.py)<br>
O código é responsável por gerenciar a lógica principal da transmissão de conteúdo. Ele integra o server_selector.py para garantir a continuidade do streaming, redirecionando requisições para o melhor servidor disponível em caso de falhas.

[`api.py`](./src/services/api.py)<br>
O arquivo expõe a lógica da seleção de servidores através de uma API REST, permitindo que outros sistemas ou clientes consultem e escolham o melhor servidor disponível para streaming.

---

### 2) Requisito Não Funcional (RNF)  
**RNF Selecionado:** **Tempo de Resolução de Falha**  

**Descrição:**  
O requisito escolhido define que, em caso de falha em um servidor de streaming, o sistema deve redirecionar as requisições para um servidor alternativo sem comprometer a experiência do usuário.   

**Critério de Qualidade:**  
- O tempo máximo permitido para a escolha de um novo servidor após uma falha deve ser de **até 100 ms**.  


**Validação do RNF:** [`test_server_selector.py`](./tests/test_server_selector.py)  

Os testes automatizados verificam se:  
- O sistema detecta falhas e seleciona um novo servidor dentro do tempo especificado.  

- A escolha do servidor prioriza a menor latência disponível.  

- O failover ocorre de forma contínua, mesmo em cenários de falhas múltiplas.  

Além disso, o arquivo [`test_api.py`](./tests/test_api.py) complementa a validação do RNF ao testar a resposta da API que gerencia a seleção de servidores.<br>

Os testes incluem:
- Verificação da disponibilidade da API para garantir que ela pode responder a solicitações sem falhas.

- Medição do tempo de resposta da API, assegurando que a troca de servidores ocorra dentro do limite de 100 ms.

- Teste de resiliência, simulando falhas e verificando se a API consegue redirecionar as requisições corretamente.

**Execução dos testes:**  
```bash
pytest test_server_selector.py 
```

```bash
pytest test_api.py
