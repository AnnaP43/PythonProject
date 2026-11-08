import logging
import os


def setup_logger(name, log_file):
    """Создает и настраивает логгер для модуля."""
    os.makedirs("logs", exist_ok=True)
    file_path = os.path.join("logs", log_file)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler(file_path, mode='w', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger