import pytest
from website.auth import password_authenticator



def test_password_validator() -> None:
    assert password_authenticator("abcDEF1") == "too short"
    assert password_authenticator("ABCDEF123!") == "missing a lowercase letter"
    assert password_authenticator("abcdef123!") == "missing an uppercase letter"
    assert password_authenticator("AbcdefgH!") == "missing a number"
    assert password_authenticator("AbcdefgH9") == "missing a special character"
    assert password_authenticator("AbcdefgH1#") == 0
    assert password_authenticator("AbcdefgH1!") == 0
    assert password_authenticator("ABCDabcd1234!@#$") == 0
    assert password_authenticator("Aa1!Bb2@Cc3#Dd4$Ee5%Ff6^Gg7&Hh8*Ii9(Jj0)Kk-Ll_Mm+Nn/OoPpQqRrSsTtUuVvWwXxYyZz") == 0
    assert password_authenticator("") == "too short"


if __name__ == "__test__":
    test_password_validator()