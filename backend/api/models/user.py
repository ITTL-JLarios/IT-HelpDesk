from pydantic import BaseModel
from typing import Annotated, Union
from enum import Enum

class Role(Enum):
    admin = "Admin"
    sup = "Supervisor"
    it = "IT"

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    role: Union[Role, None] = Role.it

class UserInDB(User):
    hashed_password: str