from ..client import Client
from ..datatypes import ApiResponse, UID

class UsersAPI:
    def __init__(self, client: Client):
        self._client = client

    def get_UID(self, nickname: str):
        """
        https://developer.eternalreturn.io/static/media/OpenAPI_KR_20251118.html#get-user-by-nickname
        """
        params = {"query": nickname}
        resp = self._client._httpClient.get(f'v1/user/nickname', params=params) \
            .json()

        return ApiResponse[UID](**resp).data