# ARQUITECTURA ORIENTADA A SERVICIOS 
## Curso 2025-26 
## Dani Pérez, Rafa Oliver, Guillem Crespo, Iván Vallespín, Sergi Hernández


## Objetivo del proyecto  

El objetivo de este proyecto es desarrollar una API de recetas de cocina utilizando FastAPI, y en fases posteriores añadiremos persistencia con base de datos y despliegue en la nube.

La API permite realizar operaciones CRUD (crear, leer, actualizar y borrar recetas):
• GET /recipes: devuelve únicamente el id y el nombre de cada receta.
• GET /recipes/{id}: devuelve el detalle completo de una receta.
• POST /recipes: crear una receta nueva.
• PUT /recipes/{id}: reemplazar receta completa.
• PATCH /recipes/{id}: actualizar parcialmente una receta.
• DELETE /recipes/{id}: borrar una receta.

La entidad principal es la “Receta”, que contiene los siguientes campos:
• id: identificador numérico de la receta
• nombre: nombre del plato
• ingredientes: lista completa de ingredientes
• pasos: lista de instrucciones de preparación
• tags: etiquetas o categorías (por ejemplo: “italiano”, “vegano”, “rápido”)
• tiempo: tiempo estimado de preparación (en minutos)
• vegana: valor booleano que indica si la receta es vegana


## Avance realizado  

En esta tercera fase hemos implementado una estructura base funcional del proyecto y todas las operaciones CRUD.
Implementaciones actuales:
• Hemos creado la carpeta app/data con el archivo recetas.json que contiene los datos persistentes de ejemplo.
• Hemos definido tres modelos en app/models/recipe.py.
o Receta → modelo completo con todos los campos.
o RecetaListado → modelo reducido utilizado para listar recetas (solo id y nombre).
o RecetaUpdate → modelo con campos opcionales para actualizar parcialmente mediante PATCH.
• Hemos implementado todas las rutas principales en app/routes/recipes.py.
• Hemos configurado el archivo main.py para montar la API.
• Las operaciones actualmente disponibles son:
o GET /recipes → devuelve la lista de recetas mostrando únicamente el id y el nombre.
o GET /recipes/{id} → muestra el detalle de una receta concreta por su identificador.
o POST /recipes → permite crear una nueva receta.
o PUT /recipes/{id} → reemplaza completamente una receta existente.
o PATCH /recipes/{id} → actualiza únicamente los campos enviados.
o DELETE /recipes/{id} → elimina una receta del archivo JSON.

A diferencia del proyecto de ejemplo, que guardaba los datos solo en memoria (lo que significa que se perdían cada vez que se reiniciaba el servidor),
en nuestro proyecto los datos se guardan de forma persistente en un archivo local app/data/recetas.json.
Esto lo conseguimos gracias a dos funciones implementadas en recipes.py:
• _load_data() → lee el contenido actual del archivo JSON y lo convierte en una lista de objetos.
• _save_data() → escribe en el archivo cualquier cambio realizado (como crear, modificar o eliminar una receta).
Por lo que, las modificaciones que se hagan a través de la API se mantienen guardadas aunque el servidor se detenga o se reinicie.

Este método de almacenamiento de datos es rápido y sencillo para una fase inicial, pero más adelante migraremos el almacenamiento a una base de datos como SQLite o Oracle y lo podríamos empaquetar con Docker para su despliegue.  


## Pasos para probar la API  

Clonar el repositorio:
• git clone https://github.com/rafaoliver5/AOS_GRUPO4.git

• cd AOS_GRUPO4

Crear y activar un entorno virtual:
• python -m venv venv
• venv\Scripts\activate

Instalar las dependencias:
• pip install -r app/requirements.txt

Ejecutar el servidor:
• uvicorn app.main:app --reload

Abrir la interfaz de pruebas de Swagger UI en el navegador:
• http://127.0.0.1:8000/docs

Desde ahí se pueden probar las operaciones disponibles:
• GET /recipes → Ver el listado de recetas (solo id y nombre).
• GET /recipes/{id} → Obtener los detalles de una receta concreta.
• POST /recipes → Crear una nueva receta.
• PUT /recipes/{id} → Modificar una receta completamente.
• PATCH /recipes/{id} → Modificar una receta parcialmente.
• DELETE /recipes/{id} → Eliminar una receta del listado.


## Próximos pasos  

• Sustituir el almacenamiento en JSON por una base de datos (SQLite o Oracle).  
• Empaquetar el proyecto con Docker y desplegarlo en la nube.  
• Añadir tests automáticos en la carpeta /test.  
• Añadir filtros opcionales en GET /recipes (texto, etiquetas, vegana) cuando migremos a base de datos.  