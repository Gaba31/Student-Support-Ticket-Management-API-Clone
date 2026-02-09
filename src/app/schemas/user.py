from pydantic import BaseModel

class UserLogin(BaseModel):
    user_name : str
    password : str


class Users(BaseModel):
    user_id: str
    user_name: str
    password : str
    