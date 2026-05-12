# 🔄 Conversor Studio

Una aplicación web minimalista y elegante construida con **Django** que permite a los usuarios convertir archivos de un formato a otro de manera rápida y segura. Cuenta con una interfaz moderna inspirada en el diseño de Apple (Glassmorphism), enfocada en la mejor experiencia de usuario (UX).

## ✨ Características

- **CSV a Excel:** Convierte fácilmente bases de datos `.csv` a hojas de cálculo `.xlsx` listas para trabajar.
- **PDF a Word:** Transforma documentos `.pdf` a archivos `.docx` editables conservando su estructura.
- **Diseño Moderno:** Interfaz responsiva, limpia y minimalista, con zona de carga visual (Drag & Drop) y retroalimentación clara.
- **Validación y Seguridad:** Límite máximo de subida de 10MB por archivo y validación de extensiones para evitar cargas maliciosas.
- **Gestión de Almacenamiento:** Sistema inteligente que limpia automáticamente los archivos temporales de los usuarios que tengan más de 1 hora de antigüedad.

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python, Django 5.x
- **Conversión de Datos:** `pandas`, `openpyxl` (CSV a Excel)
- **Conversión de Documentos:** `pdf2docx` (PDF a Word)
- **Frontend:** HTML5, CSS3 nativo (Variables CSS), Bootstrap 5

## 🚀 Instalación y Ejecución Local

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/conversor-archivos-django.git
   cd conversor-archivos-django
   ```

2. **Crear y activar un entorno virtual:**
   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar las dependencias:**
   ```bash
   pip install django pandas openpyxl pdf2docx
   ```

4. **Aplicar las migraciones de la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Abrir la aplicación:**
   Abre tu navegador web y visita `http://127.0.0.1:8000/`.

## 📂 Estructura del Proyecto

El corazón de la aplicación se encuentra en `conversor_app/`, donde `views.py` gestiona las rutas y `utils.py` maneja toda la lógica independiente de procesamiento y conversión de archivos.