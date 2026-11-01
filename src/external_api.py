import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction):
    """Принимает транзакцию и возвращает сумму в рублях, если валюта в
USD или EUR, происходит обращение к внешнему API для получения текущего
курса валют и конвертации суммы операции в рубли. """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return float(data["result"])

    return amount
