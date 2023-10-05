import pytest
from fastapi.testclient import TestClient
from app.config import settings


@pytest.mark.parametrize('to, subject, message, status_code',[
    ('dastan12151@gmail.com', 'Testing sub', 'test', 250),
    ('assgfasd1', 'das1', 'test', 422),
])
def test_email(to, subject, message, status_code, cl: TestClient):
    data = {'to': to,
            'subject': subject,
            'message': message}
    response = cl.post('/send_email', json=data)
    print(response.content)
    assert response.status_code == status_code
