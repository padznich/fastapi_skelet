"""
https://github.com/tiangolo/full-stack-fastapi-couchbase/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app/api/api_v1/endpoints/users.py
"""
import logging
from typing import List

from fastapi import APIRouter

from users.models import User, UserBase


logger = logging.getLogger()
router = APIRouter()


@router.get('/', response_model=List[User])
def read_users(skip: int = 0, limit: int = 100):
    """
    Retrieve users.
    """
    logger.info(f'skip:{skip} | limit:{limit}')
    users = [
        {
            'id': 1,
            'email': 'a@mail.com',
            'first_name': 'a',
            'last_name': 'b',
        }
    ]
    return users


@router.get('/{user_id}', response_model=User)
def read_user(user_id: int, q: str = None):
    """
    Retrieve user by id.
    """
    logger.info(f'user_id:{user_id} | {q}')
    user = {
        'id': user_id,
        'email': 'a@mail.com',
        'first_name': 'a',
        'last_name': 'b',
    }
    return user


@router.put('/{user_id}', response_model=User)
def update_user(user_id: int, user: User):
    """
    Update user by id.
    """
    logger.info(f'user_id:{user_id} | {user}')
    return user


@router.delete('/{user_id}', response_model=int)
def remove_user(user_id: int):
    """
    Remove user by id.
    """
    logger.info(f'user_id:{user_id}')
    return user_id


@router.post('/', response_model=User)
def add_user(user: UserBase):
    """
    Add user
    """
    logger.info(f'{user}')
    user = {'id': 42, **user.dict()}
    return user


@router.get("/search/", response_model=List[User])
def search_users(q: str = None, skip: int = 0, limit: int = 100):
    """
    Search users, use Bleve Query String syntax:
    http://blevesearch.com/docs/Query-String-Query/
    """
    logger.info(f'{q} | skip:{skip} | limit:{limit}')
    users = [
        {
            'id': 1,
            'email': 'a@mail.com',
            'first_name': 'a',
            'last_name': 'b',
        }
    ]
    return users
