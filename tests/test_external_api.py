from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert_to_rub


@pytest.fixture
def rub_transaction():
    """Транзакция в рублях (не требует запроса в API)."""
    return {
        "operationAmount": {
            "amount": "150.50",
            "currency": {"code": "RUB"}
        }
    }


@pytest.fixture
def usd_transaction():
    """Транзакция в долларах (требует запроса в API)."""
    return {
        "operationAmount": {
            "amount": "10.0",
            "currency": {"code": "USD"}
        }
    }


@pytest.fixture
def eur_transaction():
    """Транзакция в евро (требует запроса в API)."""
    return {
        "operationAmount": {
            "amount": "20.0",
            "currency": {"code": "EUR"}
        }
    }


def test_convert_rub(rub_transaction):
    """Проверяет: если валюта RUB, функция просто возвращает сумму.
    Никаких запросов к API быть не должно. """
    result = convert_to_rub(rub_transaction)
    assert result == 150.50


@patch("src.external_api.requests.get")


def test_convert_usd(mock_get, usd_transaction):
    """Проверяет: если валюта USD, функция делает запрос к API."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 900.0}
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    result = convert_to_rub(usd_transaction)

    assert result == 900.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_eur(mock_get, eur_transaction):
    """Проверяет: если валюта EUR, функция также делает запрос к API."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 2000.0}
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    result = convert_to_rub(eur_transaction)

    assert result == 2000.0
    mock_get.assert_called_once()
