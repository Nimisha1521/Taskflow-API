from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):    #It automatically reads configuration values from environment variables or an .env file.It helps you manage sensitive information
   
    SECRET_KEY : str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    #Tells Pydantic to read configuration values from a file named .env. If your .env file contains additional variables that are not defined in the Settings class, Pydantic ignores them instead of raising an error.


settings = Settings()




#python -c "import secrets; print(secrets.token_urlsafe(64))" to generate secret key
