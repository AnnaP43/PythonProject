import pytest

from src.widget import get_date, mask_account_card


#Тесты для проверки, что функция корректно распознает и применяет нужный
# тип маскировки в зависимости от типа входных данных (карта или счет).
@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000797356816561", "Visa Platinum 7000 79** **** 6561"),
    ("Maestro 1538768911239878", "Maestro 1538 76** **** 9878"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 65783415908778453218", "Счет **3218")
])
def test_mask_account_card_type(input_data, expected):
    assert mask_account_card(input_data) == expected

# Параметризованные тесты с разными типами карт и
# счетов для проверки универсальности функции.
@pytest.mark.parametrize("card_type, number", [
    ("Счет", "12345678901234567890"),
    ("Visa", "1234567890123456"),
    ("MasterCard", "1234567890123456789"),
    ("Maestro", "1234567890123456"),
    ("Мир", "1234567890123456"),
])
def test_mask_account_card_universality(card_type, number):
    result = mask_account_card(f"{card_type} {number}")
    assert result.startswith(card_type)
    assert "**" in result

# Тестирование функции на обработку
# некорректных входных данных и проверка ее устойчивости к ошибкам
@pytest.mark.parametrize("invalid_data", [
    "", "12345", "Счет",
])
def test_mask_account_card_invalid_input(invalid_data):
    assert mask_account_card(invalid_data) == "Некорректный ввод"


# Тестирование правильности преобразования даты.
def test_get_date_correct_conversion():
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"

# Проверка работы функции на различных входных форматах даты,
# включая граничные случаи и нестандартные строки с датами.
@pytest.mark.parametrize("date_str, expected", [
    ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ("2020-01-01T00:00:00.000000", "01.01.2020"),
    ("2024-05-11T09:26:17", "11.05.2024")
])
def test_get_date_various_formats(date_str, expected):
    assert get_date(date_str) == expected

# Проверка, что функция корректно обрабатывает входные строки,
# где отсутствует дата.
@pytest.mark.parametrize("invalid_date", [
    "2023-06-2022", "", "не дата", "2024-13-24N99:99:99"
])
def test_get_date_invalid(invalid_date):
    with pytest.raises(ValueError):
        get_date(invalid_date)
