# Proyecto: Notificaciones en Tiempo Real con SSE

Este proyecto implementa un sistema de notificaciones en tiempo real utilizando **Server-Sent Events (SSE)** en Python. SSE permite a los clientes recibir actualizaciones automáticas desde el servidor a través de una conexión HTTP persistente.

## 📌 ¿Qué es Server-Sent Events (SSE)?

SSE es una tecnología que permite a los servidores enviar datos de manera unidireccional a los clientes a través de una conexión HTTP. Es ideal para notificaciones en tiempo real, actualizaciones de datos en vivo y eventos en streaming sin la sobrecarga de WebSockets.

🔹 **Características de SSE:**
- Comunicación unidireccional desde el servidor al cliente.
- Basado en HTTP, compatible con la mayoría de navegadores y clientes HTTP.
- Uso eficiente de recursos en comparación con WebSockets.

## 📂 Estructura del Proyecto

```
📁 proyecto_sse
 ├── main.py  # Código principal de suscripción y escucha de eventos SSE
 ├── README.md  # Documentación del proyecto
 ├── requirements.txt  # Dependencias del proyecto
```

## 🚀 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/rodrigog898/Tutoriales.git
   cd Tutoritales/Server Sent Event
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```


## 🔥 Ejecución

Para ejecutar el programa y recibir notificaciones en tiempo real, usa el siguiente comando:

```bash
python main.py
```


## 📬 Notificaciones SSE

Una vez ejecutado, el sistema se suscribirá a un servidor SSE y recibirá mensajes con la siguiente estructura:

```json
{
  "tipo": "Alerta",
  "mensaje": "Se ha detectado un acceso no autorizado."
}
```

## 🛠️ Configuración Adicional

- Modifica `user_id` en `main.py` para suscribirte con diferentes usuarios.
- Asegúrate de que el servidor de notificaciones SSE está corriendo en `http://localhost:8085`.

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

✨ _¡Gracias por usar este proyecto!_ 🚀

