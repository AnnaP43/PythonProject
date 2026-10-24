def filter_by_currency(transactions, currency):
    """Принимает на вход список словарей, представляющих транзакции.
Функция должна возвращать итератор, который поочередно выдает транзакции,
где валюта операции соответствует заданной"""
    for transaction in transactions:
        transaction_currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Принимает список словарей с транзакциями и возвращает описание
    каждой операции по очереди."""
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start, end):
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    в заданном диапазоне"""
    for number in range(start, end + 1):
        card_str = str(number).zfill(16)

        formated_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"

        yield formated_card
