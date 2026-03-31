import httpx
from .config import config

class Client:
    def __init__(self, api_key: str):
        def handle_http_error(response: httpx.Response):
            # TODO: API 명세에 있는 상태 확인 후 커스텀 에러 객체 raise, message가 있는 경우 확인 가능하게
            response.raise_for_status()
            pass

        self._httpClient = httpx.Client(
            base_url= config.base_url,
            headers={
                "x-api-key": api_key
            },
            event_hooks={
                'response': [handle_http_error]
            }
        )

        from .endpoints.users import UsersAPI
        self.user = UsersAPI(self)