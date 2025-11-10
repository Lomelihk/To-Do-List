# Aplicación de Lista de Tareas (To-Do List)

Esta es una aplicación web simple pero funcional para gestionar una lista de tareas pendientes, construida con el framework Django.

## Características

-   **Autenticación de Usuarios:** Sistema completo de registro, inicio y cierre de sesión.
-   **Gestión de Tareas (CRUD):**
    -   **Crear:** Añadir nuevas tareas a la lista.
    -   **Leer:** Ver la lista completa de tareas y el detalle de cada una.
    -   **Actualizar:** Editar el título y la descripción de las tareas existentes.
    -   **Eliminar:** Borrar tareas de la lista.
-   **Interfaz de Administración:** El modelo de Tareas está integrado con el panel de administración de Django para una gestión sencilla.
-   **Seguridad (Pendiente):** La lógica para que cada usuario solo pueda ver y gestionar sus propias tareas está diseñada pero necesita ser implementada.

## Tecnologías Utilizadas

-   **Backend:**
    -   Python 3
    -   Django 5.2
-   **Base de Datos:**
    -   SQLite (para desarrollo)
-   **Frontend:**
    -   HTML5
    -   CSS (básico, sin framework)

## Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### 1. Prerrequisitos

-   Tener instalado Python 3.8 o superior.
-   Tener instalado `pip` (el gestor de paquetes de Python).

### 2. Clonar el Repositorio

```bash
git clone <URL-del-repositorio>
cd To-Do-List
```

### 3. Crear y Activar un Entorno Virtual

Es una buena práctica aislar las dependencias del proyecto en un entorno virtual.

-   **En macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
-   **En Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 4. Instalar Dependencias

Instala todas las librerías necesarias que se encuentran en el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Aplicar las Migraciones

Este comando creará la base de datos SQLite y las tablas necesarias para la aplicación.

```bash
python manage.py migrate
```

### 6. Crear un Superusuario

Para poder acceder al panel de administración de Django, necesitas crear una cuenta de administrador.

```bash
python manage.py createsuperuser
```
Sigue las instrucciones en la terminal para elegir un nombre de usuario, correo electrónico y contraseña.

## Cómo Ejecutar la Aplicación

Una vez completada la instalación, inicia el servidor de desarrollo de Django.

```bash
python manage.py runserver
```

La aplicación estará disponible en tu navegador en la siguiente dirección: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

-   Para acceder al panel de administración, ve a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e inicia sesión con las credenciales del superusuario que creaste.