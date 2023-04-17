# Task Nr.2:

# Create a class method to return the reversed string of a given string.


class StringOperations:
    @classmethod
    def get_reversed_string(cls, my_string: str) -> str:
        return my_string[::-1]


print(StringOperations.get_reversed_string("Sun is shining!"))

# Output:
# !gninihs si nuS
