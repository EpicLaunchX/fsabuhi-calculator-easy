import src.pytemplate.entrypoints.cli.main as cli


def mock_add(monkeypatch):
    inputs = iter(["1", "2", "add"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    result = cli.main()
    assert result == 3


def mock_subtract(monkeypatch):
    inputs = iter(["1", "2", "subtract"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    result = cli.main()
    assert result == -1


def mock_divide(monkeypatch):
    inputs = iter(["1", "2", "multiply"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    result = cli.main()
    assert result == 2


def mock_multiply(monkeypatch):
    inputs = iter(["1", "2", "divide"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    result = cli.main()
    assert result == 0.5
