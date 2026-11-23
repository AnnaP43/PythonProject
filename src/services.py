import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список транзакций и строку поиска.
    Возвращает список транзакций, в описании которых есть эта строка. """
    if not search:
        return []

    pattern = re.compile(re.escape(search), re.IGNORECASE)

    result = []
    for transaction in data:
        description = transaction.get("description", "")
        if description and pattern.search(description):
            result.append(transaction)

    return result


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    """Принимает список транзакций и список категорий (по полю description).
    Возвращает словарь, где ключи - названия категорий, а значения -
    количество операций в каждой категории."""
    descriptions = [
        t.get("description") for t in data if t.get("description")
    ]

    counts = Counter(descriptions)

    result = {}
    for category in categories:
        result[category] = counts.get(category, 0)

    return result
