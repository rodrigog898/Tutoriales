import requests
from requests.auth import HTTPBasicAuth

# URL de Elasticsearch para consultar
ES_URL = "http://localhost:9200/logs/_search"

# Credenciales de autenticación
USER = 'elastic'
PASSWORD = 'changeme'  # Cambia esto si tienes una contraseña diferente

# Consulta para buscar logs con nivel ERROR
query = {
  "query": {
    "match": {
      "level": "ERROR"
    }
  }
}

# Realizar la solicitud GET con autenticación
response = requests.get(ES_URL, json=query, auth=HTTPBasicAuth(USER, PASSWORD))

# Mostrar los resultados
if response.status_code == 200:
    hits = response.json()['hits']['hits']
    if hits:
        for hit in hits:
            print(hit["_source"])
    else:
        print("No se encontraron resultados para la consulta.")
else:
    print(f"Error: {response.status_code} - {response.text}")

