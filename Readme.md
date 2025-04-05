# Projeto Django com MongoDB e Celery

## O que Usei:
- **Django**: API REST
- **MongoDB**: Banco de dados NoSQL
- **Celery + Redis**: Processamento assíncrono de tarefas
- **Docker**: Contêinerização

---

## Como rodar o projeto:

### **Clonar o repositório**



## Rodar a aplicação com Docker
docker-compose up --build
## Como rodar os testes:
pytest
pytest test_integration_users.py
## Endpoints da API
Criar uma faixa etária:
POST  http://127.0.0.1:8000/api/agegroups/add/
Content-Type: application/json

{
  "label": "10-15",
  "min_age": 10,
  "max_age": 15
}

Listar todas as faixas etárias
Content-Type: application/json
GET http://127.0.0.1:8000/api/agegroups/list/

Remover uma faixa etária
Content-Type: application/json
DELETE http://127.0.0.1:8000/api/agegroups/delete/
{
  "label": "18-25"
}


