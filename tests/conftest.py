from collections.abc import Generator

import pytest
from starlette.testclient import TestClient

from fastapi_todo.app import app


@pytest.fixture(scope="module")
def client() -> Generator:
    client = TestClient(app)
    yield client

