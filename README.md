# 📦 Sistema de Gestión de Inventario (PoC)

Backend para un sistema de gestión de inventario de productos desarrollado con **FastAPI** y **PostgreSQL**, implementado con una arquitectura limpia en capas (APIs, Lógica de negocio, Acceso a datos y Base de datos).

---

## 🚀 Características

- **Gestión CRUD**: Control total de productos, categorías y proveedores.
- **Control de Ventas y Stock**: Registro de ventas con deducción automática de stock en tiempo real.
- **Operaciones Masivas**: Actualización masiva de precios y control ágil de inventario.
- **Filtros Avanzados**: Búsqueda parametrizada de productos.
- **Documentación Interactiva**: Interfaz visual Swagger/OpenAPI integrada.
- **Pruebas Automatizadas**: Suite completa de pruebas unitarias y de integración con `pytest`.

---

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.10+
- **Framework Web:** FastAPI
- **Base de Datos:** PostgreSQL
- **Contenedores:** Docker & Docker Compose
- **Testing:** Pytest

---

## 📋 Requisitos Previos

Asegúrate de tener instalado:
- [Python 3.10+](https://www.python.org/)
- [Docker](https://www.docker.com/) & Docker Compose
- [Git](https://git-scm.com/)

---

## ⚙️ Instalación y Puesta en Marcha

### 1. Clonar el repositorio
```bash
git clone https://github.com/BrahianCarrera/inventory-management-poc.git
cd inventory-management-poc
```

### 2. Crear y activar el entorno virtual
```bash
# En Windows:
python -m venv venv
venv\Scripts\activate

# En Linux / macOS:
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Iniciar la base de datos
Levanta el contenedor de PostgreSQL con Docker Compose:
```bash
docker-compose up -d
```

### 5. Ejecutar la aplicación
```bash
python main.py
```
El servidor iniciará en: `http://127.0.0.1:8000`

---

## 📖 Documentación de la API

FastAPI genera automáticamente la documentación interactiva:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Para consultar el detalle de los endpoints y modelos de petición/respuesta, revisa [endpoints_documentation.md](endpoints_documentation.md).

---

## 🧪 Pruebas

Para ejecutar la suite de pruebas automatizadas:
```bash
pytest
```
> **Nota:** La base de datos debe estar levantada mediante Docker antes de correr las pruebas.

---

## 📁 Estructura del Proyecto

```text
├── backend/
│   ├── apis/          # Controladores y rutas HTTP (FastAPI)
│   ├── data_access/   # Consultas y persistencia en PostgreSQL
│   ├── logic/         # Validaciones y reglas de negocio
│   └── models/        # Esquemas de datos con Pydantic
├── database/          # Scripts SQL de inicialización y conexión
├── tests/             # Pruebas unitarias y de integración
├── docker-compose.yml # Configuración del contenedor de PostgreSQL
├── main.py            # Punto de entrada de la aplicación
└── requirements.txt   # Dependencias del proyecto
```