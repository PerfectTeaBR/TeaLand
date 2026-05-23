from pydantic import BaseModel

class UserModel(BaseModel):
    user: str
    id: str
    mooncoins: str

class ServerModel(BaseModel):
    name: str
    id: str
    people: str
