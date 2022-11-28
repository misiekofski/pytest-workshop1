class PhoneBook:
    def __init__(self) -> None:
        self.numbers = {}

    def add(self, name, number):
        if 9 <= len(number) <= 11 and number.isdigit():
            self.numbers[name] = number
        else:
            raise ValueError("Number must contains between 9 and 11 digits")

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())
