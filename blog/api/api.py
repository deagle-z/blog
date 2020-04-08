from fastapi import APIRouter
from blog.api.routers.user import router as user_router

router = APIRouter()
router.include_router(user_router, tags=["users"], prefix="/users")
