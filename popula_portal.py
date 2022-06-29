import json
import requests
import sys


base_url = "http://localhost:8080/Plone/++api++"
username = "admin"
password = "admin"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Authenticate
response = requests.post(f"{base_url}/@login", headers=headers, json={"login": username, "password": password})

# Create Campus
responseCreate = requests.post(f"{base_url}/", headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
                               json={'@type': 'Document', 'id': 'campus4',  'title': 'Campus UFT', 'description': 'Lista de Campus da UFT'},
                               auth=('admin', 'admin'))

if response.status_code == 200:
    token = response.json()["token"]
    headers["Authorization"] = f"Bearer {token}"
    print(f"Autenticado! Token: {token}")
else:
    raise ValueError("Usuário ou senha inválidos")

if responseCreate.status_code == 201:
    data = responseCreate.json()
    path = data["@id"]
    print(f"Criado {path}")
    url = f"{path}/@workflow/publish"
    requests.post(url, headers=headers)
else:
    raise ValueError("Não Criado")
