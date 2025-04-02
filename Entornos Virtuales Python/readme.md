
## 💻 Configuración del Entorno Virtual

Sigue estos pasos para configurar un entorno virtual en Python antes de instalar dependencias:

### 1. Crear el entorno virtual llamado `geninter`

```bash
python -m venv geninter
```

### 2. Activar el entorno virtual

- **En macOS/Linux:**

```bash
source geninter/bin/activate
```

- **En Windows:**

```bash
geninter\Scripts\activate
```

### 3. Instalar dependencias del proyecto

Una vez activado el entorno, ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará todas las librerías necesarias definidas en el archivo `requirements.txt`.
