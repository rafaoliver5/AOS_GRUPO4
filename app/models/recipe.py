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
