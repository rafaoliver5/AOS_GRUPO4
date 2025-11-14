# ARQUITECTURA ORIENTADA A SERVICIOS 
## Curso 2025-26 
## Dani Pérez, Rafa Oliver, Guillem Crespo, Iván Vallespín, Sergi Hernández


## Objetivo del proyecto  

El objetivo de este proyecto es desarrollar una API de recetas de cocina utilizando FastAPI, y en fases posteriores añadiremos persistencia con base de datos y despliegue en la nube.  

La API permitirá realizar operaciones CRUD (crear, leer, actualizar y borrar recetas):  
    • GET /recipes: lista y búsqueda (por texto, tag, vegana).  
    • GET /recipes/{id}: detalle.  
    • POST /recipes: crear receta.  
    • PUT /recipes/{id}: reemplazar receta completa.  
    • PATCH /recipes/{id}: actualizar una receta.  
    • DELETE /recipes/{id}: borrar receta.  

La entidad principal es la “Receta”, que contiene los siguientes campos:  
    • id: identificador numérico de la receta  
    • nombre: nombre del plato  
    • ingredientes: lista de ingredientes  
    • pasos: lista de instrucciones de preparación  
    • tags: etiquetas o categorías (por ejemplo: “italiano”, “vegano”, “rápido”)  
    • tiempo: tiempo estimado de preparación (en minutos)  
    • vegana: valor booleano que indica si la receta es vegana  


## Avance realizado  

En esta tercera fase hemos implementado una estructura base funcional del proyecto y todas operaciones CRUD.  
Implementaciones actuales:  
    • Hemos creado la carpeta app/data con el archivo recetas.json que contiene datos de ejemplo.  
    • Hemos definido el modelo Receta en app/models/recipe.py.  
    • Hemos implementado las rutas principales en app/routes/recipes.py.  
    • Hemos configurado el archivo main.py para montar la API.  
    • Las operaciones actualmente disponibles son:  
        o GET /recipes → lista todas las recetas almacenadas en el JSON.  
        o GET /recipes/{id} → muestra el detalle de una receta concreta por su identificador.  
        o DELETE /recipes/{id} → elimina una receta del archivo JSON.
        o POST /recipes → permite crear una nueva receta.
        o PUT /recipes/{id} → reemplaza completamente una receta existente.
        o PATCH /recipes/{id} → actualiza únicamente los campos enviados. 
        

A diferencia del proyecto de ejemplo, que guardaba los datos solo en memoria (lo que significa que se perdían cada vez que se reiniciaba el servidor),  
en nuestro proyecto los datos se guardan de forma persistente en un archivo local app/data/recetas.json.  
Esto lo conseguimos gracias a dos funciones implementadas en recipes.py:  
    • _load_data() → lee el contenido actual del archivo JSON y lo convierte en una lista de objetos.  
    • _save_data() → escribe en el archivo cualquier cambio realizado (como borrar o añadir una receta).  
Por lo que, las modificaciones que se hagan a través de la API (por ejemplo, al eliminar una receta) se mantienen guardadas aunque el servidor se detenga o se reinicie.  
Este método de almacenamiento de datos es rápido y sencillo para una fase inicial, pero hemos pensado que más adelante el almacenamiento lo migraremos a una base de datos como SQLite o Oracle y lo podríamos empaquetar con Docker para su despliegue.  


## Pasos para probar la API  

1. Clonar el repositorio:  
    • git clone https://github.com/rafaoliver5/AOS_GRUPO4.git  
    • cd AOS_GRUPO4  
2. Crear y activar un entorno virtual:  
    • python -m venv venv  
    • venv\Scripts\activate  
3. Instalar las dependencias:  
    • pip install -r app/requirements.txt  
4. Ejecutar el servidor:  
    • uvicorn app.main:app --reload  
5. Abrir la interfaz de pruebas de Swagger UI en el navegador:  
    • http://127.0.0.1:8000/docs  
6. Desde ahí se pueden probar las operaciones disponibles:  
    • GET /recipes → Ver el listado completo de recetas.  
    • GET /recipes/{id} → Buscar una receta por su ID.  
    • DELETE /recipes/{id} → Eliminar una receta del listado.
    • POST /recipes → Crear una nueva receta.
    • PUT /recipes/{id} → Reemplazar una receta completa.
    • PATCH /recipes/{id} → Actualizar parcialmente una receta. 


## Próximos pasos  
 
    • Incorporar filtros en GET /recipes para buscar por texto, etiqueta o si es vegana.  
    • Sustituir el almacenamiento en JSON por una base de datos (SQLite o Oracle).  
    • Empaquetar el proyecto con Docker y desplegarlo en la nube.  
    • Añadir tests automáticos en la carpeta /test.  