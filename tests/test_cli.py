import src.pytemplate.entrypoints.cli.main as cli


def test_add():
    assert cli.main(1, 2, "add") == 3


def test_subtract():
    assert cli.main(1, 2, "subtract") == -1


def test_divide():
    assert cli.main(1, 2, "divide") == 0.5


def test_multiply():
    assert cli.main(1, 2, "multiply") == 2
