import requests

BASE_URL = "http://127.0.0.1:8000"

def test_register_user_success():
    user = {
        "name": "Teste Usuário",
        "cpf": "99999999999",
        "age": 30
    }
    response = requests.post(f"{BASE_URL}/api/users/", json=user)
    assert response.status_code == 200 or response.status_code == 400  # 400 se já existe
    if response.status_code == 200:
        assert "mensagem" in response.json()
    elif response.status_code == 400:
        assert "erro" in response.json() and "CPF" in response.json()["erro"]

def test_register_user_missing_fields():
    user = {
        "name": "Sem CPF",
        "age": 20
    }
    response = requests.post(f"{BASE_URL}/api/users/", json=user)
    assert response.status_code == 400
    assert "erro" in response.json()

def test_user_status_existing():
    cpf = "99999999999"
    response = requests.get(f"{BASE_URL}/api/status/{cpf}/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "cpf" in data
    assert "track" in data

    
def test_user_status_not_found():
    cpf = "00000000000"  
    response = requests.get(f"{BASE_URL}/api/status/{cpf}/")
    assert response.status_code == 404
    assert "erro" in response.json()
