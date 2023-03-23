# Task Nr.4:

# Lets say we have classes: A, B and C:

# Modify the program to add a method say_hello to class A that prints "Hello from class A".
# Modify the program to add a method say_hello to class B that prints "Hello from class B".
# Modify the program to add a method say_hello to class C that prints "Hello from class C".
# Create an object of class C and call the say_hello method on it. What is the output?
# Modify the program so that class B's say_hello method calls the say_hello method of class A using the super() function.
# Create an object of class C and call the say_hello method on it again. What is the output now?


class A:
    def say_hello(self) -> None:
        print("Hello from class A")


class B(A):
    def __init__(self) -> None:
        super().__init__()

    def say_hello(self) -> None:
        print("Hello from class B")


class C(B):
    def say_hello(self) -> None:
        print("Hello from class C")


object_of_class_c = C()
object_of_class_c.say_hello()
