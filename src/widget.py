from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """обрабатывает информацию о картах и счетах"""
    if not info:
        return "Некорректный ввод"

    #разделяем строку на 2 части
    parts = info.rsplit(" ", 1)

    if len(parts) != 2:
        return "Некорректный ввод"

    card_type, number = parts

    if "Счет" in card_type:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """Принимает строку с датой в формате '2024-03-11T02:26:18.671407'
 и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    parsed_date = datetime.fromisoformat(date_str)
    return parsed_date.strftime("%d.%m.%y")
