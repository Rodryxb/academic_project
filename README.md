# Sistema de Gestión Académica - Backend con Django & DRF

Proyecto desarrollado para la asignatura de Desarrollo Backend, consistente en un sistema que implementa un modelo Entidad-Relación, una API REST construida con Django REST Framework (DRF) y un frontend web estilizado con Bootstrap que consume los datos de forma asíncrona mediante JavaScript (`fetch`).

---

## 🚀 Características del Proyecto

* **API RESTful:** Endpoints configurados mediante `ModelViewSet` de DRF para la gestión de Docentes (`teachers`), Asignaturas (`courses`) y Estudiantes (`students`).
* **Interfaz Web Dinámica:** Vistas HTML maquetadas con Bootstrap que enmascaran los endpoints de la API y realizan consultas asíncronas con `fetch()`.
* **Solución a Rutas No Encontradas:** Manejo personalizado de la ruta raíz (`/`) y ruta comodín (catch-all) para evitar los errores 404 por defecto de Django.
* **Sistema de Autenticación:** Módulo de inicio y cierre de sesión integrado (`login` / `logout`).
* **Precarga de Datos (Fixtures):** Carga inicial de datos de prueba mediante archivos JSON estructurados.

---

## 🛠️ Tecnologías Utilizadas

* **Python**
* **Django**
* **Django REST Framework (DRF)**
* **Bootstrap 5.3** (CDN)
* **SQLite** (Base de datos)

---

## 📦 Instrucciones de Instalación y Ejecución

Sigue estos pasos para clonar y ejecutar el proyecto localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Rodryxb/academic_project.git](https://github.com/Rodryxb/academic_project.git)
   cd academic_project
