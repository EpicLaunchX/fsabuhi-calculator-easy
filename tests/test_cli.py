from unittest import mock

from src.pytemplate.entrypoints.cli.main import main


def test_add():
    inputs = iter(["6", "2", "add"])
    with mock.patch("builtins.input", lambda: next(inputs)):
        result = main()
        assert result == 8


def test_subtract():
    inputs = iter(["1", "2", "subtract"])
    with mock.patch("builtins.input", lambda: next(inputs)):
        result = main()
        assert result == -1


def test_divide():
    inputs = iter(["1", "2", "multiply"])
    with mock.patch("builtins.input", lambda: next(inputs)):
        result = main()
        assert result == 2


def test_multiply():
    inputs = iter(["1", "2", "divide"])
    with mock.patch("builtins.input", lambda: next(inputs)):
        result = main()
        assert result == 0.5
