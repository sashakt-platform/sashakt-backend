from fastapi import APIRouter

from app.api.routes import location, login, organization, private, roles, users, utils
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(utils.router)
api_router.include_router(roles.router)
api_router.include_router(organization.router)
api_router.include_router(location.router)


if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)
