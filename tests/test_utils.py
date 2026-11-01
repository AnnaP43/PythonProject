import json

import pytest

from src.utils import read_json_file


def test_read_missing_file():
    """Возвращает пустой список, если файла нет."""
    assert read_json_file("data/no_such_file.json") == []

@pytest.mark.parametrize(
    "content, expected_result",
    [
        (json.dumps([{"id": 1}, {"id": 2}]), [{"id": 1}, {"id": 2}]),

        ("это просто текст, а не JSON", []),

        (json.dumps({"id": 1}), []),
    ]
)
def test_read_json_scenarios(tmp_path, content, expected_result):
    """ Проверяет разные варианты содержимого файла.
    Благодаря parametrize, этот код выполнится 3 раза. """
    file = tmp_path / "test.json"
    file.write_text(content, encoding="utf-8")

    assert read_json_file(str(file)) == expected_result
