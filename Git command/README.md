# 🛠️ Comandos básicos de Git

Este documento contiene una descripción de los comandos más comunes de Git y su utilidad. Git es un sistema de control de versiones distribuido que ayuda a gestionar el código de manera eficiente.

---

## 🚀 Inicializar un repositorio

- **`git init`**  
  🌀 Crea un nuevo repositorio local.

---

## 🔍 Verificar cambios

- **`git diff`**  
  🧐 Muestra los cambios que aún no se han preparado (staged).

- **`git status`**  
  📋 Lista los archivos nuevos o no modificados en el repositorio.

---

## ➕ Añadir cambios

- **`git add .`**  
  ➡️ Añade todos los archivos modificados al área de preparación (staging area).

- **`git add <archivo>`**  
  ➡️ Añade un archivo específico al área de preparación.

---

## ✅ Confirmar cambios

- **`git commit -a`**  
  💾 Realiza un commit de todos los cambios en los archivos que están siendo rastreados.

- **`git commit`**  
  🗂️ Confirma los cambios previamente preparados.

- **`git commit --amend`**  
  ✏️ Modifica el último commit con cambios adicionales.

---

## 🕒 Ver historial

- **`git log`**  
  📜 Muestra el historial completo de cambios en el repositorio.

---

## 🌿 Trabajo con ramas

- **`git checkout <rama>`**  
  🔄 Cambia a una rama específica y actualiza el directorio de trabajo.

- **`git branch <nueva-rama>`**  
  🌱 Crea una nueva rama.

- **`git branch -d <rama>`**  
  🗑️ Elimina una rama específica.

---

## 🌐 Trabajar con repositorios remotos

- **`git fetch <remoto>`**  
  ⬇️ Descarga todas las ramas desde un repositorio remoto.

- **`git pull <remoto> <rama>`**  
  🔄 Descarga y combina la versión remota de una rama con la local.

- **`git push <remoto> <rama>`**  
  ⬆️ Sube los cambios confirmados a un repositorio remoto.

---

## 🧩 Combinar y reorganizar ramas

- **`git merge <rama>`**  
  🔗 Fusiona una rama específica con la rama actual.

- **`git rebase <rama>`**  
  🔄 Reorganiza tu rama actual sobre la rama especificada.

---

## 🛑 Revertir cambios

- **`git revert <commit>`**  
  🚫 Crea un nuevo commit para revertir el commit especificado.

---

### 🎨 Créditos
Basado en el esquema creado por [@NikkiSiapno](https://twitter.com/NikkiSiapno) y [@ChrisStaud](https://twitter.com/ChrisStaud).
