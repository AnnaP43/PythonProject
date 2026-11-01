import pytest

from src.decorators import log


def test_log_to_console_success(capsys):
    """Проверка, что в консоль выводиться 'ок' при успешном выполнении"""
    @log()
    def my_func(a, b):
        return a+b

    my_func(1,2)
    captured = capsys.readouterr()

    assert "my_func ok" in captured.out

def test_log_to_error(capsys):
    """Проверка, что при оошибке в консоль пишеться имя функции,
    тип и входные параметры"""

    @log()
    def error_func(x):
        return 10/x

    with pytest.raises(ZeroDivisionError):
        error_func(0)

    captured = capsys.readouterr()

    assert "error_func error: ZeroDivisionError" in captured.out
    assert "Inputs: (0,), {}" in captured.out

def test_log_to_file_success(tmp_path):
    """Проверка, что при успешном выполенинии лог пишеться в файл.
    Вместо capsys создаем временную папку для теста"""
    log_file = tmp_path / "test_log.txt"

    @log(filename=log_file)

    def my_func(x, y):
        return x*y

    my_func(3, 4)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "my_func ok" in content

def test_log_to_file_error(tmp_path):
    """Проверка, что при ошибке лог пишеться в файл"""
    log_file = tmp_path / "error_log.txt"

    @log(filename=log_file)
    def error_func(a, b):
        return a+b

    with pytest.raises(TypeError):
        error_func("текст", 5)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "error_func error: TypeError" in content
    assert "Inputs: ('текст', 5), {}" in content



