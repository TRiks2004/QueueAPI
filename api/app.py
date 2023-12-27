from fastapi import FastAPI

from common.setting import settings


def create_app():
    
    app = FastAPI(
        debug=settings.debug,
        docs_url='/api/help',
        title='FastApi Queue',
    )

    return app
# source ~/.bashrc 
# docker compose -f api.yaml up -d