from enum import Enum
from typing import List

from pydantic import BaseModel, constr, EmailStr


class Roles(Enum):
    user = 'user'
    admin = 'admin'
    guest = 'guest'


class Groups(Enum):
    developers = 'developers'
    admins = 'admins'
    sales = 'sales'
    clients = 'clients'
    guests = 'guests'


class User(BaseModel):
    id: int
    email: EmailStr
    first_name: constr(max_length=63)
    last_name: constr(max_length=63)
    role: Roles = Roles.guest
    groups: List[Groups] = [Groups.guests]
