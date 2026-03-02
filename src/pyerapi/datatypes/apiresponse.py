from typing import Any, TypeVar, Generic
from pydantic import BaseModel, model_validator

T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    code: int
    message: str
    data: T

    @model_validator(mode="before")
    @classmethod
    def extract_dynamic_data(cls, values: dict[str, Any]):
        if "data" not in values:
            extra_keys = set(values) - {"code", "message"}
            if len(extra_keys) == 1:
                key = extra_keys.pop()
                values["data"] = values.pop(key)
        return values