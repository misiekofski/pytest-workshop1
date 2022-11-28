class PhoneBook:
    def __init__(self) -> None:
        self.__numbers: dict = {}

    def add(self, name: str, number: str) -> None:
        if (9 <= len(number) <= 11) and number.isdigit():
            self.__numbers[name] = number
        else:
            raise ValueError('Number is not correct!')

    def lookup(self, name: str) -> None:
        return self.__numbers[name]

    def names(self) -> set:
        return set(self.__numbers.keys())
