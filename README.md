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

### Zadanie 2

### Zadanie 3

### Zadanie 4

### Zadanie 5