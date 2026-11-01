import json
import os


def read_json_file(file_path):
    """Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                return data
            else:
                return []

    except (json.JSONDecodeError, Exception):
        return []
