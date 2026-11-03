from src.logger_config import setup_logger


logger = setup_logger("masks", "masks.log")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.debug(f"Запущена маскировка карты: {card_number}")

    result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    logger.info("Карта успешно замаскирована")
    return result


def get_mask_account(account_number: str) -> str:
    """Функция маскировки банковского счета"""
    logger.debug(f"Запущена маскировка счета: {account_number}")

    result = f"**{account_number[-4:]}"

    logger.info("Счет успешно замаскирован")
    return result
