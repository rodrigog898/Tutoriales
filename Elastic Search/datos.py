import requests
import json
from datetime import datetime
import random
from requests.auth import HTTPBasicAuth

# URL de Elasticsearch
ES_URL = "http://localhost:9200/logs/_doc/"

# Credenciales de autenticación
USER = 'elastic'
PASSWORD = 'changeme'  # Cambia esto si tienes una contraseña diferente

# Niveles de log
log_levels = ["INFO", "DEBUG", "ERROR", "WARN"]

# Generar 1000 registros de log
for i in range(1000):
    log = {
        "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        "level": random.choice(log_levels),
        "message": f"This is a test log message {i}"
    }

    # Realizar la solicitud POST con autenticación básica
    response = requests.post(ES_URL, json=log, auth=HTTPBasicAuth(USER, PASSWORD))

    if response.status_code == 201:
        print(f"Log {i} inserted successfully")
    else:
        print(f"Error inserting log {i}: {response.status_code} - {response.text}")

