# You are given an input array of bigrams, and an array of words. Write a function that returns True if every single bigram from this array can be found at least once in an array of words.

# Example:

# can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ True
# can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ False
# # "cu" does not exist in any of the words.
# can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True
# can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) ➞ False



def can_find(bigrams: list, words: list) -> bool:
    return all(bigram in ' '.join(words) for bigram in bigrams)

    

    # logic = True
    # for bigram in bigrams:
    #     if bigram in words:
    #         print(bigram)
    #         logic = True
    #     else:
    #         logic = False
    # return logic
print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))

