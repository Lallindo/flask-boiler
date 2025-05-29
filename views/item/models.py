from pydantic import BaseModel

class ItemBase(BaseModel):
    id: int
    nome: str