from fastapi import APIRouter, HTTPException
from typing import List
from pathlib import Path
import json

from app.models.recipe import Receta

router = APIRouter(prefix="/recipes", tags=["Recipes"])

# Ruta del archivo JSON donde se guardan las recetas
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "recetas.json"

# Función auxiliar para leer los datos del archivo JSON
def _load_data() -> List[dict]:
    if not DATA_PATH.exists():
        return []  # si el archivo no existe, devuelve una lista vacía
    with DATA_PATH.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)  # lee el contenido y lo convierte en lista de Python
        except json.JSONDecodeError:
            return []  # si el archivo está vacío o tiene error, devuelve una lista vacía

# Función auxiliar para guardar los datos en el archivo JSON
def _save_data(data: List[dict]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)  # crea la carpeta /data si no existe
    with DATA_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)  # sobrescribe el archivo con los nuevos datos

# GET route para listar todas las recetas
@router.get("/", response_model=List[Receta])
def list_recipes():
    return _load_data()

# GET route para obtener una receta por su id
@router.get("/{recipe_id}", response_model=Receta)
def get_recipe(recipe_id: int):
    data = _load_data()
    for r in data:
        if r.get("id") == recipe_id:
            return r
    raise HTTPException(status_code=404, detail="Receta no encontrada")

# DELETE route para eliminar una receta por su id
@router.delete("/{recipe_id}", status_code=204)
def delete_recipe(recipe_id: int):
    data = _load_data()
    new_data = [r for r in data if r.get("id") != recipe_id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    _save_data(new_data)
    return

