import pytest
from pb.phonebook import PhoneBook


@pytest.fixture
def empty_phonebook() -> PhoneBook:
    return PhoneBook()


@pytest.fixture
def populated_phonebook() -> PhoneBook:
    pb = PhoneBook()
    pb.add('Rossmann', '123456789')
    pb.add('Missing', '1234567890')