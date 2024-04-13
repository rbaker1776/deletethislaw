import pytest
from website.auth import is_password_valid



def test_password_validator() -> None:
    assert is_password_valid("") == False
    assert is_password_valid("abcdefgh") == False
    assert is_password_valid("Abcdefgh") == False
    assert is_password_valid("A2cdefgh") == False
    assert is_password_valid("A2#defgh") == True


def test_all() -> None:
    test_password_validator()


if __name__ == "__test__":
    test_all()