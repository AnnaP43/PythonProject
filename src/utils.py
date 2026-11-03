import json
import os
from src.logger_config import setup_logger


logger = setup_logger("utils", "utils.log")


def read_json_file(file_path):
    """Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""


    logger.debug(f"Запуск чтения файла: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно прочитан. Записей: {len(data)}")
                return data
            else:
                logger.warning(f"Файл {file_path} не содержит список")
                return []
    except Exception as e:
        logger.error(f"Ошибка при чтении JSON: {e}")
        return []
