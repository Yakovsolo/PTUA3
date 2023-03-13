from random_word import RandomWords

def print_random_word(word_numbers: int) -> list:
    random_word_list = []
    for i in range(word_numbers):
        random_word_list.append(RandomWords().get_random_word())
    capitised_list = [word.upper() for word in random_word_list]
    sorted_list = sorted(capitised_list)
    return sorted_list

word_numbers = int(input("Enter the number of words you want to generate: "))
        
print(print_random_word(word_numbers))
