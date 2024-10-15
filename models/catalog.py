from pydantic import BaseModel

class Catalog(BaseModel):
    id: str
    name: str
    description: str
    category: str
    price: float

