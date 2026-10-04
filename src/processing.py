def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и опционально значение для ключа state.
Функция возвращает новый список словарей, содержащий только те словари,
у которых ключ state соответствует указанному значению"""


    filtered_list = []


    for item in data:
        if item.get("state") == state:
            filtered_list.append(item)

    return filtered_list


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Принимает список словарей и возвращает отсортированный
    по дате список"""

    return sorted(data, key=lambda item: item["date"], reverse=reverse)