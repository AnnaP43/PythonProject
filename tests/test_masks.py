import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование правильности маскирования номера карты.
def test_get_mask_card_number_correct_masking():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

# Проверка работы функции на различных входных форматах номеров карт,
# включая граничные случаи и нестандартные длины номеров.
@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("5678349012346682324", "5678 34** **** 2324"),
    ("123456789012345", "1234 56** **** 2345"),
    ("5678", "5678 ** **** 5678"),
])
def test_get_mask_card_number_various_formats(card_number, expected):
    assert get_mask_card_number(card_number) == expected

# Проверка, что функция корректно обрабатывает входные строки,
# где отсутствует номер карты.
def test_get_mask_card_number_empty_input():
    assert get_mask_card_number("") == " ** **** "


# Тестирование правильности маскирования номера счета.
def test_get_mask_account_correct_masking():
    assert get_mask_account("12345678901234567890") == "**7890"

# Проверка работы функции с различными форматами и длинами номеров счетов.
@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("123456789012345", "**2345"),
    ("12345", "**2345"),
])
def test_get_mask_account_various_formats(account_number, expected):
    assert get_mask_account(account_number) == expected

#Проверка, что функция корректно обрабатывает входные данные,
# где номер счета меньше ожидаемой длины.
def test_get_mask_account_short_length():
    assert get_mask_account("123") == "**123"
    assert get_mask_account("1") == "**1"
    assert get_mask_account("") == "**"
