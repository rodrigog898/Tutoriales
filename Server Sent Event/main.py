import json
import requests
from sseclient import SSEClient

def verify_subscription(user_id):
    url = f"http://localhost:8085/ruta/servicio/a/suscribrirse/{user_id}"
    try:
        response = requests.get(url, stream=True, timeout=5)
        if response.status_code == 200:
            print(f"✅ Suscripción exitosa para usuario: {user_id}\n")
            return response
        else:
            print(f"❌ Error al suscribirse: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None

def listen_notifications(user_id):
    response = verify_subscription(user_id)
    if response is None:
        return
    
    messages = SSEClient(response.url)
    
    for msg in messages:
        if msg.data:
            try:
                notification = json.loads(msg.data)
                handle_notification(notification)
            except json.JSONDecodeError:
                print("⚠️ Mensaje no válido:", msg.data)

def handle_notification(notification):
    tipo = notification.get('tipo', 'Desconocido')
    mensaje = notification.get('mensaje', 'Sin mensaje')
    
    print(f"\n🔔 Nueva notificación [{tipo}]:")
    print(mensaje)

if __name__ == "__main__":
    listen_notifications("mail@gmail.com")
