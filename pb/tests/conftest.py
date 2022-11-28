from pb.phonebook import PhoneBook
import pytest


@pytest.fixture
def empty_phonebook():
    return PhoneBook()


@pytest.fixture
def populated_phonebook():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "123456789")
    phonebook.add("Missing", "123456781")
    phonebook.add("Missing", "123456782")
    return phonebook
