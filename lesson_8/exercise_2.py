# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and 15 letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word_list_one = []
for number_of_words in range(5):
    x = random.randint(5, 15)
    random_word = ''.join(random.choices(letters, k = x))
    word_list_one.append(random_word)
print(word_list_one)

answer_dict = {}

for letter in letters:
    count = 0
    for word in word_list_one:
        if letter in word:
            count += 1
        answer_dict.update({letter: count})

print(answer_dict)


       



