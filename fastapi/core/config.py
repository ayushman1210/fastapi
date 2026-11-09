from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    Database_url:str="postgresql+async_driver://postgres:Aas%402010@localhost/Hello"

    class config:
        env_file=".env"

settings=Settings()
