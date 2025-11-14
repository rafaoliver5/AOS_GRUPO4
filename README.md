ARQUITECTURA ORIENTADA A SERVICIOS
Curso 2025-26

Dani Pérez, Rafa Oliver, Guillem Crespo, Iván Vallespín, Sergi Hernández

Objetivo del proyecto

El objetivo de este proyecto es desarrollar una API de recetas de cocina utilizando FastAPI, y en fases posteriores añadir persistencia con base de datos y despliegue en la nube.

La API permite realizar operaciones CRUD:

GET /recipes → devuelve únicamente el id y el nombre de cada receta.

GET /recipes/{id} → devuelve el detalle completo de una receta.

POST /recipes → crea una receta nueva.

PUT /recipes/{id} → reemplaza completamente una receta existente.

PATCH /recipes/{id} → actualiza parcialmente una receta.

DELETE /recipes/{id} → elimina una receta.

Campos del modelo Receta

id — identificador numérico

nombre — nombre del plato

ingredientes — lista de ingredientes

pasos — lista de instrucciones

tags — etiquetas (p. ej., “vegano”, “rápido”, “italiano”)

tiempo — tiempo estimado de preparación

vegana — booleano que indica si la receta es vegana

Avance realizado

En esta fase hemos desarrollado la estructura completa del proyecto e implementado todas las operaciones CRUD.

Implementaciones actuales:

Carpeta app/data con el archivo persistente recetas.json.

Modelos definidos en app/models/recipe.py:

Receta — modelo completo

RecetaListado — modelo reducido (solo id y nombre)

RecetaUpdate — modelo para actualizaciones parciales (PATCH)

Rutas implementadas en app/routes/recipes.py.

API montada en app/main.py.

Endpoints disponibles:

GET /recipes → lista reducida de recetas

GET /recipes/{id} → detalle de una receta

POST /recipes → crear receta

PUT /recipes/{id} → reemplazar una receta

PATCH /recipes/{id} → modificar parcialmente

DELETE /recipes/{id} → eliminar receta

Persistencia

A diferencia del proyecto de ejemplo, donde los datos se perdían tras reiniciar el servidor, en nuestro proyecto el contenido se almacena en un archivo JSON local.

Funciones principales:

_load_data() → lee el archivo JSON

_save_data() → guarda los cambios en disco

En un futuro se migrará este sistema a una base de datos (SQLite u Oracle).

Pasos para probar la API
1. Clonar el repositorio
git clone https://github.com/rafaoliver5/AOS_GRUPO4.git
cd AOS_GRUPO4

2. Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate

3. Instalar dependencias
pip install -r app/requirements.txt

4. Ejecutar el servidor
uvicorn app.main:app --reload

5. Abrir Swagger UI

http://127.0.0.1:8000/docs

6. Probar los endpoints

GET /recipes

GET /recipes/{id}

POST /recipes

PUT /recipes/{id}

PATCH /recipes/{id}

DELETE /recipes/{id}

Próximos pasos

Migrar el almacenamiento JSON a base de datos (SQLite u Oracle)

Empaquetar con Docker

Desplegar en la nube

Añadir tests automáticos

Ampliar filtros (por texto, etiquetas, vegana) tras la migración