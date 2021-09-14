from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

URL = '/api/v1'


def test_converter_valid_input():
    response = client.get(f"{URL}/convert?from_currency=USD&to_currency=GHS&amount=501")
    assert response.status_code == 200
    data = response.json()
    assert data['from_currency'] == 'USD'
    assert data['to_currency'] == 'GHS'
    assert data['original_amount'] == 501
    assert isinstance(data['converted_amount'], float)


def test_converter_invalid_input():
    response = client.get(f"{URL}/convert?from_currency=USDT&to_currency=GHS&amount=501")
    assert response.status_code == 500
    assert response.json() == {
                                "detail": "Conversion failed due to invalid inputs"
                                }