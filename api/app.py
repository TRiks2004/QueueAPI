from fastapi import FastAPI

from common.setting import settings

from models.datebase import engine
from models.models import Base

from services import routers 

def create_app():
    # Тест
    Base.metadata.create_all(bind=engine)

    app = FastAPI(
        debug=settings.debug,
        docs_url='/api/help',
        title='FastApi Queue',
    )

    app.include_router(
        router=routers.APIRouterItem,
        prefix='/items',
    )

    app.include_router(
        router=routers.APIRouterUser,
        prefix='/users',
    )

    return app

# source ~/.bashrc 
# docker compose -f api.yaml up -d

    