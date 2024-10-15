from pydantic import BaseModel, Field
from uuid import uuid4

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description="A unique identifier for the user")
    username: str 
    password: str
