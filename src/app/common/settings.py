import os

from typing import Type, Tuple, Iterator, Optional, List, Union
from pydantic import AnyHttpUrl

from dotenv import load_dotenv
from pathlib import Path

from functools import lru_cache
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)

ROOT_DIR = Path(__file__).parent.parent.parent.parent  # This is the Project Root

# 환경 파일 로드
load_dotenv()


def env_file() -> Iterator[str]:
    env = os.getenv("ENV", "local").lower()

    if env in {"production", "prod", "prd"}:
        envs = (".env", ".env.prd", ".env.prod", ".env.production")
    elif env in {"staging", "stage", "stg"}:
        envs = (".env", ".env.stg", ".env.stage", ".env.staging")
    elif env in {"testing", "test", "tst", "local"}:
        envs = (".env", ".env.local", ".env.tst", ".env.test", ".env.testing")
    else:
        envs = (".env",)

    envs = list(os.path.join(ROOT_DIR, file_name) for file_name in envs)

    print(f"Loaded env files: {list(envs)}")
    return iter(envs)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file(),
        extra="ignore",
        env_file_encoding="utf-8",
    )
    print(f"model_config: {model_config}")

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: Type[BaseSettings],  # noqa: ARG003
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,  # noqa: ARG003
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            dotenv_settings,
            env_settings,
            file_secret_settings,
        )

    project_name: str = ""

    routes: Optional[List[dict]] = []
    backend_cors_origins: List[Union[str, AnyHttpUrl]] = ["http://localhost", "http://localhost:3000"]

    env: str = ""

    @property
    def environment(self) -> str:
        env = None

        if env in {"production", "prod", "prd"}:
            env = "production"
        elif env in {"staging", "stg"}:
            env = "staging"
        elif env in {"testing", "test", "tst"}:
            env = "testing"
        else:
            env = "development"

        return env

    @property
    def is_test(self) -> bool:
        return self.env in ("test", "testing", "tst", "local")

    @property
    def is_dev(self) -> bool:
        return self.env in ("dev", "development", "dev")

    @property
    def is_stg(self) -> bool:
        return self.env in ("staging", "stage", "stg")

    @property
    def is_prd(self) -> bool:
        return self.env in ("production", "prod", "prd")


@lru_cache()
def get_settings() -> Settings:

    return Settings()
