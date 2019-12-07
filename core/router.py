from fastapi import APIRouter

from users.views import router as users_views

api_router = APIRouter()
api_router.include_router(users_views, prefix="/users", tags=["users"])
