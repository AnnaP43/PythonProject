import pandas as pd


def read_csv_transactions(file_path):
    """Читает финансовые операции из CSV-файла и возвращает список словарей.
    Принимает путь к файлу."""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict("records")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def read_excel_transactions(file_path):
    """Читает финансовые операции из Excel-файла (XLSX) и возвращает список словарей.
    Принимает путь к файлу."""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict("records")
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []
