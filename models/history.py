from pydantic import BaseModel

class History(BaseModel):
    id: str
    username: str
    purchase: str
    views: str
    likes: str