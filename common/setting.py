import pathlib

from pydantic_settings import BaseSettings
import environ


BASE_DIR = pathlib.Path(__file__).parent.parent

env = environ.Env()
environ.Env.read_env(env_file=BASE_DIR / '.env')


class Settings(BaseSettings):
    debug: bool = env.bool('DEBUG', default=False)

class SettingsDatabase(Settings):
    db_host: str = env.str('DB_HOST')
    db_port: str = env.str('DB_PORT')
    db_user: str = env.str('DB_USER')
    db_password: str = env.str('DB_PASSWORD')
    db_name: str = env.str('DB_NAME')
    
    db_uri: str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

settings = Settings()
settings_database = SettingsDatabase()