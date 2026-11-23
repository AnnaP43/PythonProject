import pytest

from src.services import process_bank_operations, process_bank_search


@pytest.fixture
def sample_transactions():
    """Тестовые данные для проверки функций."""
    return [
        {"id": 1, "description": "Перевод организации", "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 2, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 3, "description": "Открытие вклада", "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 4, "description": "Перевод организации", "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 5, "description": "Перевод с карты на карту", "operationAmount": {"currency": {"code": "EUR"}}},
    ]


def test_process_bank_search_success(sample_transactions):
    """Проверяет успешный поиск по слову (без учета регистра)."""
    result = process_bank_search(sample_transactions, "перевод")
    assert len(result) == 4
    assert all("перевод" in t["description"].lower() for t in result)


def test_process_bank_search_not_found(sample_transactions):
    """Проверяет, что при отсутствии слова возвращается пустой список."""
    result = process_bank_search(sample_transactions, "ипотека")
    assert result == []


def test_process_bank_search_empty_query(sample_transactions):
    """Проверяет, что пустой запрос возвращает пустой список."""
    assert process_bank_search(sample_transactions, "") == []


def test_process_bank_operations(sample_transactions):
    """Проверяет подсчет операций по категориям."""
    categories = ["Перевод организации", "Открытие вклада", "Несуществующая категория"]
    result = process_bank_operations(sample_transactions, categories)

    assert result["Перевод организации"] == 2
    assert result["Открытие вклада"] == 1
    assert result["Несуществующая категория"] == 0
