import pytest

from pb.phonebook import PhoneBook

class TestPhoneBook:
    def test_lookup_by_name(self, empty_phonebook: PhoneBook):
        empty_phonebook.add("Rossmann", "123456789")
        assert "123456789" == empty_phonebook.lookup("Rossmann")


    def test_phonebook_contains_all_names(self, populated_phonebook: PhoneBook):
        assert populated_phonebook.names() == {"Rossmann", "Missing"}


    @pytest.mark.parametrize(
        'number, result', (('12345678', 0), ('123456789012', 0))
    )
    def test_len_number(self, empty_phonebook: PhoneBook, number: str, result: int):
        with pytest.raises(ValueError):
            empty_phonebook.add('Rossmann', number)

        assert len(empty_phonebook.names()) == result
