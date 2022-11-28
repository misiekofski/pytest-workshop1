class PhoneBook:
    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        number: str = str(number)
        if not number.isnumeric():
            raise ValueError(f"Numer telefonu nie jest liczbowy!. Podany ciąg: {number}")
        if len(number) > 11 or len(number) < 9:
            raise ValueError(f'Numer telefonu powinien zawierać od 9 do 11 cyfr! Podany ciąg: {len(number)}: {number}')
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self) -> set:
        return set(self.numbers.keys())

