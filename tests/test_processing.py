import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def sample_date():
    """Фикстура с данными, включающими различные комбинации state, date"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-01-02T11:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03T12:00:00"},
        {"id": 4, "state": "CANCELED", "date": "2023-01-04T13:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
    ]

@pytest.fixture()
def empty_date():
    """Фикстура для проверки с пустыми списокм"""
    return []


@pytest.fixture()
def invalid_date():
    """Фикстура с некорректными датами"""
    return [
        {"id": 1, "date": "неверный формат"},
        {"id": 2, "date": "2023-13-45T99:99:99"},
    ]

# Тестирование фильтрации списка словарей по заданному статусу state.
def test_filter_by_state_correct_filtering(sample_date):
    result = filter_by_state(sample_date, "EXECUTED")
    assert  len(result) == 3
    for item in result:
        assert  item["state"] == "EXECUTED"

# Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
def test_filter_by_state_no_matching_status(sample_date):
    result = filter_by_state(sample_date, "UNKNOWN_STATE")
    assert result == []

# Параметризация тестов для различных возможных значений статуса state.
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 3),
    ("PENDING", 1),
    ("CANCELED", 1),
])
def test_filter_by_state_parametrized(sample_date, state, expected_count):
   result = filter_by_state(sample_date, state)
   assert len(result) == expected_count
   for item in result:
       assert item["state"] == state

# Проверка на пустой список
def test_filter_by_state_empty_list(empty_date):
    assert filter_by_state(empty_date) == []


# Тестирование сортировки списка словарей
# по датам в порядке убывания и возрастания.
def test_sort_by_date_descending(sample_date):
    result = sort_by_date(sample_date)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)

def test_sort_by_date_ascending(sample_date):
    result = sort_by_date(sample_date, reverse=False)
    dates = [item["date"]for item in result]
    assert dates == sorted(dates, reverse=False)

# Проверка корректности сортировки при одинаковых датах.
def test_sort_by_date_same_dates(sample_date):
    result = sort_by_date(sample_date)
    count = 0

    for item in result:
        if item["date"] == "2023-01-01T10:00:00":
            count += 1

    assert count == 2

# Тесты на работу функции с некорректными или нестандартными форматами дат.
def test_sort_by_date_invalid_formats(invalid_date):
    result = sort_by_date(invalid_date)
    assert isinstance(result, list)