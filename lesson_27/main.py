# def say_hello() -> None:
#     print("hello")


# greet = say_hello

# greet()  # print 'hello'

# from collections.abc import Callable


# def say_hello(name: str) -> None:
#     print(f"hello {name}!")


# def another_function(f: Callable, *args) -> None:
#     f(*args)


# another_function(say_hello, "fool")

# print((lambda x: [x, x**2, x**3])(2))

# print((lambda x: (x, x**2, x**3))(3))
# # (3, 9, 27)
# print((lambda x: [x, x**2, x**3])(3))
# # [3, 9, 27]
# print((lambda x: {1: x, 2: x**2, 3: x**3})(3))
# # {1: 3, 2: 9, 3: 27}

# print(f"---{(lambda s: s[::-1])('Hello')}---")

numbers = [1, 2, 3, 4, 5]

list(map(str, numbers))


def custom_map(function, iterable):
    from functools import reduce

    return reduce(
        lambda items, value: items + [function(value)],
        iterable,
        [],
    )


print(list(custom_map(str, numbers)))
