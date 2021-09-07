from starlette.testclient import TestClient


todo_data = {
    "text": "test text",
    "completed": False,
}


def test_when_unauthorized_user_wants_to_add_todo_then_ti_should_pass_error(client: TestClient):
    subject = client.post(
        "/api/v1/todos",
        json=todo_data,
    )
    assert subject.status_code == 401
