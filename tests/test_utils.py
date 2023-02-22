import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "address",
    ["ayrton@sato.com", "john@doe.com"],
)
def test_positive_check_valid_email(address):
    """Ensure email is valid"""
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize(
    "address",
    ["ayrton@.com", "j@.com" "+@com"],
)
def test_negative_check_invalid_email(address):
    """Ensure email is invalid"""
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Test generation of random simple passwords
    TODO: Generate hashed complex passwords, encrypt it
    """
    passwords = []
    for i in range(100):
        passwords.append(generate_simple_password(8))
    assert (len(set(passwords))) == 100
