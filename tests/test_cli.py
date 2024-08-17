from unittest import mock

import src.pytemplate.entrypoints.cli.main as cli


def test_add(monkeypatch):
    inputs = iter(["1", "2", "add"])
    mock.patch("builtins.input", lambda: next(inputs))
    result = cli.main()
    assert result == 3


def test_subtract(monkeypatch):
    inputs = iter(["1", "2", "subtract"])
    mock.patch("builtins.input", lambda: next(inputs))
    result = cli.main()
    assert result == -1


def test_divide(monkeypatch):
    inputs = iter(["1", "2", "multiply"])
    mock.patch("builtins.input", lambda: next(inputs))
    result = cli.main()
    assert result == 2


def test_multiply(monkeypatch):
    inputs = iter(["1", "2", "divide"])
    mock.patch("builtins.input", lambda: next(inputs))
    result = cli.main()
    assert result == 0.5
