¡Claro! Aquí tienes todo formateado correctamente en un archivo Markdown listo para usarse como `README.md`:

```markdown
# 🚀 Despliegue de una Aplicación React en Google App Engine

Guía paso a paso para desplegar una aplicación React estática en Google App Engine usando Google Cloud Platform (GCP).

---

## 🛠 Herramientas Utilizadas

- [`create-react-app`](https://create-react-app.dev/)
- [Google Cloud Platform (GCP)](https://cloud.google.com/)
- Google Cloud Shell
- Google Cloud Storage (Buckets)

---

## ✅ Requisitos Previos

- Node.js y npm instalados.
- Cuenta de Google Cloud con un proyecto creado.

---

## 📦 Pasos para el Despliegue

### 1. Crear una App React

```bash
npx create-react-app test-app
```

Esto crea una carpeta `test-app` con todos los archivos base del proyecto.

---

### 2. Generar el Build de Producción

```bash
cd test-app
npm run build
```

Se generará una carpeta `build/` que contiene la versión optimizada para producción.

---

### 3. Crear un Bucket en GCP

1. Ve a la consola de GCP.
2. Accede a **Storage > Buckets**.
3. Crea un nuevo bucket (puedes dejar los valores por defecto).
4. Anota el nombre del bucket. Ejemplo: `straight-veld-8658`.

---

### 4. Subir Archivos al Bucket

1. Ingresa al bucket.
2. Sube la carpeta `build/` completa.
3. También sube el archivo `app.yaml` (creado en el siguiente paso).

---

### 5. Crear el Archivo `app.yaml`

Este archivo le indica a App Engine cómo servir los archivos estáticos.

Crea un archivo llamado `app.yaml` con el siguiente contenido:

```yaml
runtime : nodejs18
handlers:
- url: /(.*\..+)$
  static_files: build/\1
  upload: build/(.*\..+)$

- url: /.*
  static_files: build/index.html
  upload: build/index.html
```

⚠️ Asegúrate de que los paths apuntan correctamente a la carpeta `build`.

Sube este archivo al bucket.

---

### 6. Acceder a Google Cloud Shell

1. Entra al proyecto desde la consola de GCP.
2. Haz clic en el ícono de terminal > **Activate Cloud Shell**.

---

### 7. Sincronizar Archivos del Bucket al Entorno

Ejecuta los siguientes comandos en la terminal de Cloud Shell:

```bash
mkdir test-app
gsutil rsync -r gs://straight-veld-8658 ./test-app
cd test-app
```

Esto sincroniza los archivos del bucket a tu entorno en la nube.

---

### 8. Desplegar la Aplicación

En la misma terminal, ejecuta:

```bash
gcloud app deploy
```

Esto iniciará el proceso de despliegue.

Una vez completado, se mostrará un mensaje con la URL de tu app. Normalmente será:

```
https://[your-project-id].appspot.com
```

---

## 🎉 ¡Listo!

Tu aplicación React ya está en línea, corriendo en la infraestructura de Google. Puedes compartir el enlace o asociarlo con un dominio personalizado desde la consola de GCP.

---

## 🧼 Limpieza Opcional

Si deseas eliminar tu app o recursos luego de probar:

```bash
gcloud app browse                # Abrir app en navegador
gcloud app services delete default  # Eliminar servicio
```

---

