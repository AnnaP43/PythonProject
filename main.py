from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def main() -> None:
    # Пример для проверки работы функций
    examples = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]

    for item in examples:
        print(item)
        print(f"Выход: {mask_account_card(item)}\n")

    date_str = "2024-03-11T02:26:18.671407"
    print(f"Вход: {date_str}")
    print(f"Выход: {get_date(date_str)}")

    # проверки для processing.py
    test_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]

    print(f"\nФильтр: {filter_by_state(test_data)}")
    print(f"Сортировка по дате: {sort_by_date(test_data)}")

    # проверка для generators.py
    print("ПРОВЕРКА ГЕНЕРАТОРОВ")

    transactions = [
        {
            "id": 939719570,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 873106923,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 142264268,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]

    # 1. Проверка filter_by_currency
    print("\n1. Фильтрация по USD:")
    usd_transactions = filter_by_currency(transactions, "USD")
    for transaction in usd_transactions:
        print(f"  ID: {transaction['id']}, Описание: {transaction['description']}")

    # 2. Проверка transaction_descriptions
    print("\n2. Описания транзакций:")
    descriptions = transaction_descriptions(transactions)
    for desc in descriptions:
        print(f"  {desc}")

    # 3. Проверка card_number_generator
    print("\n3. Генерация номеров карт (от 1 до 5):")
    for card in card_number_generator(1, 5):
        print(f"  {card}")


if __name__ == "__main__":
    main()
