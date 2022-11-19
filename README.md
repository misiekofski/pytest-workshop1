## Instrukcja instalacji i dry run:

1. Utwórz venv (albo i nie ;))
2. `pip install -r requirements.txt`
3. W konsoli (w folderze głównym) odpal `pytest` i sprawdź czy pierwszy test przechodzi.

Powinieneś zobaczyć mniej więcej taki output:
```
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.10.2, pytest-7.2.0, pluggy-1.0.0
rootdir: C:\Users\dobrz\PycharmProjects\pytest-workshop1
collected 1 item

pb\tests\test_phonebook_basics.py .                                                                                                                                                                                              [100%] 

========================================================================================================== 1 passed in 0.02s ==========================================================================================================
```

## Struktura projektu
```bash
pytest-workshop1
│   README.md # ten plik
│   .gitignore # tego nie chcemy w repo
│   requirements.txt # plik z dependencjami do instalacji przez pipa
│   
└───pb # moduł z apliakcją phonebook
    │   phonebook.py # plik z klasą PhoneBook
    └─── tests # podfolder z plikami testowymi (pytest je znajdzie sam)
```

## Zadania warsztatowe
Do wykonania samodzielnie.

### Zadanie 1
1. Do klasy PhoneBook dodaj metodę `names()` która zwróci set wszystkich kluczy słownika `numbers`
2. Utwórz nowy test który sprawdzi działanie metody (możesz skopiować ten poniżej):
```python 
def test_phonebook_contains_all_names():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "123456789")
    assert phonebook.names() == {"Rossmann", "Missing"}
```
3. Uruchom test (w konsoli lub w PyCharmie), jaki jest rezultat?
4. Napraw test bez dotykania linijki z asercją (czego brakuje?)

### Zadanie 2
1. Dopisz walidator który w momencie dodawania numeru do książki (pod dowolnym kluczem) sprawdzi czy ciąg znaków jest cyframi (o długości między 9 a 11 cyfr)
2. Kod powinien **rzucać wyjątkiem ValueError** w przypadku próby dodania błędnego numeru
3. Napisz dwa osobne testy który spróbują dodać do książki (testy nie mają się spodziewać wyjątku):
   1. 8 cyfrowy numer
   2. 12 cyfrowy numer
4. Jako asercji użyj sprawdzenia długości setu `names()` (powinien być zero)
5. Uruchom testy, czy dojdziemy do asercji?


### Zadanie 3
1. Napisz fixturę `empty_phonebook` która zwróci pusty obiekt PhoneBook()
2. Zrefaktoryzuj wszystkie 3 testy, tak żeby używały fixtury


### Zadanie 4
1. Napisz fixturę `populated_phonebook` która zwróci obiekt PhoneBook() z kluczami `Rossmann` oraz `Missing`
2. Zrefaktoryzuj kod testu z zadania numer 1, tak żeby używał fixtury `populated_phonebook`

### Zadanie 5
1. Zrefaktoryzuj dwa testy z zadania 2 (dla 8 i 12 cyfr) używając dekoratora `@pytest.mark.parametrize`
2. Uruchom testy i sprawdź czy wszystko działa

### Zadanie 6
1. Usuń `try expect` z kodu testu zadania 5.
2. Popraw test z zadania 5 tak aby spodziewał się wyjątku.
3. Uruchom testy i sprawdź czy przechodzą
4. Zmień typ spodziewanego wyjątku w teście na inny (np. `FileNotFoundError`) i uruchom test jeszcze raz.