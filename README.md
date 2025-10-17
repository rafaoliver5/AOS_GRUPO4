# ARQUITECTURA ORIENTADA A SERVICIOS 
## Curso 2025-26 
## Dani Pérez, Rafa Oliver, Guillem Crespo, Iván Vallespín, Sergi Hernández


Nuestra primera idea de proyecto es crear una API de recetas.
La entidad principal sería la “Receta”, con un identificador y campos sencillos: nombre, lista de ingredientes, pasos, etiquetas, tiempo estimado, y si es vegana. El objetivo es que el acceso sea directo desde cualquier cliente (web o móvil) y que los datos estén lo bastante
estructurados como para poder filtrar por texto, por etiqueta o por si es vegetariana.

En esta primera fase, hemos pensado en guardar la información en un archivo JSON dentro del propio proyecto
(data/recetas.json) porque es rápido y no añade mucha complejidad. Pero más adelante podríamos migrar a SQLite o
Oracle y empaquetarlo con Docker si hace falta.

A nivel de funcionamiento la API tendrá estas operaciones básicas CRUD: consultar el listado de recetas y el detalle de
una receta concreta (GET), crear recetas nuevas (POST), reemplazar una receta completa (PUT), actualizar algunos
campos (PATCH) y borrar una receta (DELETE). Es decir, el flujo típico sería así: el usuario crea una receta, luego la busca
o la filtra, más tarde la corrige si cambia un paso, y finalmente la elimina si ya no le interesa.

Entidad principal: Receta: id, nombre, ingredientes[], pasos[], tags[], tiempo, vegana.

GET /recipes: lista y búsqueda (por texto, tag, vegana).

GET /recipes/{id}: detalle.

POST /recipes: crear receta.

PUT /recipes/{id}: reemplazar receta completa.

PATCH /recipes/{id}: actualizar una receta.

DELETE /recipes/{id}: borrar receta.
