from src.csv_excel_reader import read_csv_transactions, read_excel_transactions
from src.processing import filter_by_state, sort_by_date
from src.services import process_bank_search
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная логика программы, связывающая функционал модулей."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    print("\nВыберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    transactions = []
    if choice == "1":
        print("\nДля обработки выбран JSON-файл.")
        transactions = read_json_file("data/operations.json")
    elif choice == "2":
        print("\nДля обработки выбран CSV-файл.")
        transactions = read_csv_transactions("data/transactions.csv")
    elif choice == "3":
        print("\nДля обработки выбран XLSX-файл.")
        transactions = read_excel_transactions("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор. Завершение работы.")
        return

    if not transactions:
        print("\nНе удалось прочитать файл или он пуст.")
        return

    # Фильтрация по статусу
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_input = input("Пользователь: ").upper()

        if status_input in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, status_input)
            print(f'Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Статус операции "{status_input}" недоступен.')

    # Сортировка по дате
    print("\nОтсортировать операции по дате? Да/Нет")
    sort_choice = input("Пользователь: ").lower()

    if sort_choice == "да":
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        order = input("Пользователь: ").lower()

        if order == "по убыванию" or order == "убывание":
            transactions = sort_by_date(transactions, reverse=True)
        else:
            transactions = sort_by_date(transactions, reverse=False)

    # Фильтрация по рублям
    print("\nВыводить только рублевые транзакции? Да/Нет")
    rub_choice = input("Пользователь: ").lower()
    if rub_choice == "да":
        transactions = [
            t for t in transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    # Поиск по описанию
    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
    search_choice = input("Пользователь: ").lower()
    if search_choice == "да":
        search_word = input("Введите слово для поиска: ")
        transactions = process_bank_search(transactions, search_word)

    # Вывод результата
    print("\nРаспечатываю итоговый список транзакций...\n")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}\n")

    for t in transactions:
        # Получаем данные безопасно
        date = get_date(t.get("date", ""))
        desc = t.get("description", "Без описания")
        amount_info = t.get("operationAmount", {})
        amount = amount_info.get("amount", "0")
        currency = amount_info.get("currency", {}).get("name", "")

        from_acc = t.get("from")
        to_acc = t.get("to")

        print(f"{date} {desc}")

        # Выводим маскированные счета/карты
        if from_acc and to_acc:
            print(f"{mask_account_card(from_acc)} -> {mask_account_card(to_acc)}")
        else:
            if from_acc:
                print(mask_account_card(from_acc))
            if to_acc:
                print(mask_account_card(to_acc))

        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
