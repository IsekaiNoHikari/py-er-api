import httpx
from .config import config

class Client:
    def __init__(self, api_key: str):
        self._httpClient = httpx.Client(
            base_url= config.base_url,
            headers={
                "x-api-key": api_key
            }
        )

        from .endpoints.users import UsersAPI
        self.user = UsersAPI(self)