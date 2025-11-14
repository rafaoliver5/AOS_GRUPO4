from fastapi import APIRouter, HTTPException
from typing import List
from pathlib import Path
import json

from app.models.recipe import Receta, RecetaListado, RecetaUpdate

router = APIRouter(prefix="/recipes", tags=["Recipes"])

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "recetas.json"


# ---------------------- Funciones internas ---------------------- #

def _load_data() -> List[dict]:
    if not DATA_PATH.exists():
        return []
    with DATA_PATH.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def _save_data(data: List[dict]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with DATA_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# --------------------------- RUTAS ------------------------------ #

# GET /recipes -> lista solo con id y nombre
@router.get("/", response_model=List[RecetaListado])
def list_recipes():
    data = _load_data()
    # Transformamos cada receta completa en solo id + nombre
    return [{"id": r.get("id"), "nombre": r.get("nombre")} for r in data]


# GET /recipes/{id} -> detalle con todos los campos
@router.get("/{recipe_id}", response_model=Receta)
def get_recipe(recipe_id: int):
    data = _load_data()
    for r in data:
        if r.get("id") == recipe_id:
            return r
    raise HTTPException(status_code=404, detail="Receta no encontrada")


# POST /recipes -> crear nueva receta
@router.post("/", response_model=Receta, status_code=201)
def create_recipe(recipe: Receta):
    data = _load_data()

    # Comprobar que no exista ya ese id
    if any(r.get("id") == recipe.id for r in data):
        raise HTTPException(
            status_code=400,
            detail="Ya existe una receta con ese id",
        )

    data.append(recipe.dict())
    _save_data(data)
    return recipe


# PUT /recipes/{id} -> reemplazar receta completa
@router.put("/{recipe_id}", response_model=Receta)
def replace_recipe(recipe_id: int, recipe: Receta):
    data = _load_data()

    for idx, r in enumerate(data):
        if r.get("id") == recipe_id:
            nueva = recipe.dict()
            # El id final será el del path
            nueva["id"] = recipe_id
            data[idx] = nueva
            _save_data(data)
            return nueva

    # Si no existe la receta con ese id:
    raise HTTPException(status_code=404, detail="Receta no encontrada")


# PATCH /recipes/{id} -> actualizar parcialmente
@router.patch("/{recipe_id}", response_model=Receta)
def update_recipe(recipe_id: int, updates: RecetaUpdate):
    data = _load_data()

    for idx, r in enumerate(data):
        if r.get("id") == recipe_id:
            stored = r.copy()
            update_data = updates.dict(exclude_unset=True)

            # Aplicamos solo los campos que han llegado en el body
            stored.update(update_data)

            # Nos aseguramos de no cambiar el id
            stored["id"] = recipe_id

            data[idx] = stored
            _save_data(data)
            return stored

    raise HTTPException(status_code=404, detail="Receta no encontrada")


# DELETE /recipes/{id} -> borrar receta
@router.delete("/{recipe_id}", status_code=204)
def delete_recipe(recipe_id: int):
    data = _load_data()
    new_data = [r for r in data if r.get("id") != recipe_id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    _save_data(new_data)
    return

