from fastapi import FastAPI

def create_app():
    app = FastAPI(
        debug=True,
        docs_url='/api/help',
        title='FastApi Queue',
    )
    return app