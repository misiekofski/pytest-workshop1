from pb.phonebook import PhoneBook


def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "123456789")
    assert "123456789" == phonebook.lookup("Rossmann")


def test_phonebook_contains_all_names():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "123456789")
    assert phonebook.names() == {"Rossmann", "Missing"}

