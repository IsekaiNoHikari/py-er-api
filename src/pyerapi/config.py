from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    base_url: str = "https://open-api.bser.io"

config = Config()