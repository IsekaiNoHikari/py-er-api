from pydantic import BaseModel

class UID(BaseModel):
    userId: str
    nickname: str