from typing import List


def sum_of_numbers(number_one: int, number_two: int, number_three: int) -> int:
    return number_one + number_two + number_three


def sum_of_list_of_numbers(*args) -> int:
    return sum(args)


# skaiciu_suma(2, 6, 4, 78, 1, 454, 30, 68)


def max_number(*args) -> int:
    return max(args)


# didziausias_skaicius(2, 5, 7, 9, 5, 12, 45, 900, 1000, 12)


def reversed_sentence(sentence: str) -> str:
    sentence_words = sentence.split()
    reversed_list = sentence_words[::-1]
    return " ".join(reversed_list)


# sakinys_atvirksciai("Jau pavasaris atėjo, kas čia plytų tiek pridėjo?")


def unique_only(*args):
    return list(set(args))


# Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.


def is_number_in_list(number: int, list_of_numbers: List[int]) -> bool:
    return number in list_of_numbers


# ar_yra(5, [5, 6, 7, 9, 10, 15, 45, 100])


def count_sentence_elements(sentence: str) -> str:
    words = len(sentence.split())
    numbers = sum(char.isdigit() for char in sentence)
    upper_letters = sum(char.isupper() for char in sentence)
    lower_letters = sum(char.islower() for char in sentence)
    return f"Number of words: {words}, Number of digits: {numbers}, Number of upper letters: {upper_letters}, Number of lower letters: {lower_letters}"


# patikrinti_sakini("12: Jau pavasaris atėjo, kas čia plytų TIEK pridėjo?")


def even_numbers(start: int, finish: int) -> List[int]:
    """
    Atspausdina visus paduoto rėžio (nuo… iki) lyginius skaičius
    :param nuo: Mažiausias rėžio skaičius
    :param iki: Didžiausias rėžio skaičius
    :return: Lyginių skaičių sąrašas
    """
    list_of_numbers = []
    for number in range(start, finish + 1):
        if number % 2 == 0:
            list_of_numbers.append(number)
    return list_of_numbers
