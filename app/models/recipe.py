from pydantic import BaseModel, Field
from typing import List, Optional

class Receta(BaseModel):
    id: int = Field(..., ge=1)             
    nombre: str
    ingredientes: List[str] = []
    pasos: List[str] = []
    tags: List[str] = []
    tiempo: Optional[int] = None           
    vegana: Optional[bool] = None

class RecetaListado(BaseModel):
    id: int
    nombre: str


class RecetaUpdate(BaseModel):
    # Para PATCH: todos los campos opcionales, sin id
    nombre: Optional[str] = None
    ingredientes: Optional[List[str]] = None
    pasos: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    tiempo: Optional[int] = None
    vegana: Optional[bool] = None
