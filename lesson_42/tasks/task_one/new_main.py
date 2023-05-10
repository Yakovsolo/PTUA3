# Sukurkite ir išsibandykite funkcijas, kurios:

# 1. Gražinti trijų paduotų skaičių sumą.

from typing import List
import calendar
import datetime


def sum_of_numbers(*args) -> int:
    return sum(args)


# 2. Gražintų paduoto sąrašo iš skaičių, sumą.


def sum_of_list_of_numbers(list_of_numbers: List[int]) -> int:
    return sum(list_of_numbers)


# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).


def max_number(*args):
    return max(args)


# 4. Gražintų paduotą stringą atbulai.


def reversed_sentence(sentence: str) -> str:
    return sentence[::-1]


# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.


def count_sentence_elements(sentence: str) -> str:
    words = len(sentence.split())
    numbers = sum(char.isdigit() for char in sentence)
    upper_letters = sum(char.isupper() for char in sentence)
    lower_letters = sum(char.islower() for char in sentence)
    return f"Number of words: {words}, Number of digits: {numbers}, Number of upper letters: {upper_letters}, Number of lower letters: {lower_letters}"


# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.


def unique_only(*args):
    return list(set(args))


# 7. Gražintų, ar paduotas skaičius yra pirminis.


def is_prime_number(number: int) -> bool:
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False


# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo


def reversed_sentence_order(sentence: str):
    words = sentence.split()[::-1]
    return " ".join(words)


# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.


def is_leap(year: int):
    return calendar.isleap(year)


# 10. Gražina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.


def check_data(any_date: str):
    input_date = datetime.datetime.strptime(any_date, "%Y-%m-%d %X")
    now = datetime.datetime.now()
    time_delta = now - input_date
    return time_delta
