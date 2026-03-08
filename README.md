# Sistema de Reservas de Salas - ITM

Este proyecto es un microservicio desarrollado con FastAPI para la gestión y registro de reservas de salas académicas. Permite registrar nuevas reservas y consultar las existentes en tiempo real a través de una API REST.

## Integrantes: 
Sebastián Ladino - Emmanuel Urrego Gómez

## Características

Framework: FastAPI.
Validación de Datos: Pydantic Models.
Almacenamiento: Memoria volátil (Lista de Python).
Documentación: Autogenerada con Swagger UI.
Instalación y Configuración: Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.Clonar el repositorio, git clone https://github.com/SebasLadino16/Taller_1.git

2.cd Taller_1

3.Crear y activar el entorno virtual:python -m venv venv o con virtualenv

## En Windows (Git Bash):

source venv/Scripts/activate

Instalar dependencias: pip install -r requirements.txt o pip install "fastapi[standard]"

Ejecutar el servidor:uvicorn main:app --reload
 
## Uso de la API: 
Una vez el servidor esté corriendo, accede a la documentación interactiva en: http://127.0.0.1:8000/docs 


## Estructura del Proyecto

main.py: Lógica del servidor y definición de rutas (Endpoints).

models.py: Definición del modelo de datos Reserva usando Pydantic.

test_data.json: Archivo con ejemplos de datos para pruebas.

.gitignore: Archivo para excluir carpetas innecesarias (como venv/).

El proyecto se desarrolló bajo un flujo de trabajo colaborativo usando Git. Sebas:Creación de modelos de datos, configuración inicial y datos de prueba.Emmanuel: Implementación de endpoints POST/GET y lógica de almacenamiento.