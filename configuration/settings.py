from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN1_ID: int
    ADMIN2_ID: int
    CHANNEL_ID: str
    CHANNEL1_TO_CHECK: str
    CHANNEL2_TO_CHECK: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )


settings = Settings()
