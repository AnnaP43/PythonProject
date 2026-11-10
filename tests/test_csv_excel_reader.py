from unittest.mock import MagicMock, patch

from src.csv_excel_reader import read_csv_transactions, read_excel_transactions


@patch("src.csv_excel_reader.pd.read_csv")


def test_read_csv_transactions(mock_read_csv):
    """Тестирует чтение CSV с использованием Mock.
    Проверяет, что функция возвращает список словарей."""
    mock_df = MagicMock()

    mock_df.to_dict.return_value = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]

    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("fake_path.csv")

    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    mock_read_csv.assert_called_once_with("fake_path.csv")


@patch("src.csv_excel_reader.pd.read_excel")


def test_read_excel_transactions(mock_read_excel):
    """ Тестирует чтение Excel с использованием Mock."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"id": 3, "amount": 300}
    ]
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("fake_path.xlsx")

    assert result == [{"id": 3, "amount": 300}]
    mock_read_excel.assert_called_once_with("fake_path.xlsx")


@patch("src.csv_excel_reader.pd.read_csv")


def test_read_csv_error(mock_read_csv):
    """Проверяет обработку ошибки."""
    mock_read_csv.side_effect = Exception("Ошибка чтения")

    result = read_csv_transactions("bad_file.csv")

    assert result == []