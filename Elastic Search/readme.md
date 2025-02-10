# Proyecto: Instalación de Elastic con Docker

Este proyecto configura un entorno con **Elasticsearch**, **Kibana** y **Cerebro** utilizando Docker y Docker Compose para facilitar su despliegue.

## Características

- 📌 Implementación rápida con Docker
- ⚡ Monitoreo y gestión con Kibana y Cerebro
- 🔧 Configuración segura y persistencia de datos

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto:

```bash
# Clonar el repositorio
git clone https://github.com/rodrigog898/Tutoriales.git

# Entrar al directorio del proyecto
cd Tutoriales/Elastic Search

# Levantar los servicios con Docker Compose
docker-compose up -d
```

## Comandos útiles

#### Crear un índice en Elasticsearch

```bash
curl -X PUT "localhost:9200/logs" -u elastic:changeme -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "properties": {
      "timestamp": { "type": "date" },
      "level": { "type": "keyword" },
      "message": { "type": "text" }
    }
  }
}
'
```

#### Crear un usuario en Elasticsearch

```bash
curl -u elastic:changeme -X POST "http://localhost:9200/_security/user/kibana_user" -H 'Content-Type: application/json' -d'
{
  "password": "kibana.2025",
  "roles": ["kibana_system"],
  "full_name": "Kibana User",
  "email": "kibana_user@example.com",
  "enabled": true
}
'
```

#### Configurar Git

```bash
git config --global user.email "ro.aravenac@gmail.com"
git config --global user.name "rodrigog898"
```

## Accesos

- **Cerebro:** [http://localhost:9000/](http://localhost:9000/)
  - Usuario: `elastic`
  - Contraseña: `changeme`

- **Kibana:** [http://localhost:5601/](http://localhost:5601/)
  - Usuario: `kibana_user`
  - Contraseña: `kibana.2025`

- **Elasticsearch:** [http://localhost:9200/](http://localhost:9200/)
  - Usuario: `elastic`
  - Contraseña: `changeme`

## Contribución

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature-nueva`).
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---

✨ _¡Gracias por contribuir y usar este proyecto!_ 🚀

