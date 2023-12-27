import pathlib

from pydantic_settings import BaseSettings
import environ


BASE_DIR = pathlib.Path(__file__).parent.parent

env = environ.Env()
environ.Env.read_env(env_file=BASE_DIR / '.env')


class settings(BaseSettings):
    debug: bool = env.bool('DEBUG', default=False)


settings = settings()