import pytest

from pb.phonebook import PhoneBook


@pytest.fixture
def empty_phonebook():
    return PhoneBook()


@pytest.fixture
def populated_phonebook():
    phone_book = PhoneBook()
    phone_book.add("Rossmann", "123456789")
    phone_book.add("Missing", "123456789")

    return phone_book
