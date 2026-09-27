from src.widget import mask_account_card, get_date


def main() -> None:
    # Пример для проверки работы функций
    examples = ["Maestro 1596837868705199",
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


if __name__ == "__main__":
    main()
