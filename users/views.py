"""
https://github.com/tiangolo/full-stack-fastapi-couchbase/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app/api/api_v1/endpoints/users.py
"""
from typing import List

from fastapi import APIRouter

from users.models import User

router = APIRouter()


@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100):
    """
    Retrieve users.
    """
    users = [
        {
            'id': 1,
            'email': 'a@mail.com',
            'first_name': 'a',
            'last_name': 'b',
        }
    ]
    return users


@router.get("/search/", response_model=List[User])
def search_users(q: str = None, skip: int = 0, limit: int = 100):
    """
    Search users, use Bleve Query String syntax:
    http://blevesearch.com/docs/Query-String-Query/
    """
    users = [
        {
            'id': 1,
            'email': 'a@mail.com',
            'first_name': 'a',
            'last_name': 'b',
        }
    ]
    return users
