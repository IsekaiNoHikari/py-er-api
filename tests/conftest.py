import pytest
from pyerapi import Client

def pytest_addoption(parser):
    parser.addoption(
        "--api-key",
        action="store",
        help="API key for eternal return API",
    )

@pytest.fixture()
def client(request):
    key = request.config.getoption("--api-key")
    if not key:
        raise RuntimeError("--api-key is required")
    return Client(key)