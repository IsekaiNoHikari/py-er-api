from ..client import Client
from ..datatypes import ApiResponse, UID

class UsersAPI:
    def __init__(self, client: Client):
        self._client = client

    def get_UID(self, nickname: str):
        params = {"query": nickname}
        resp = self._client._httpClient.get(f'v1/user/nickname', params=params) \
            .raise_for_status() \
            .json()

        return ApiResponse[UID](**resp).data