# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname

#     def say_hello(self) -> None:
#         print(f"Hello, {self.name} {self.surname}")


# person = Person("first", "person")
# person.say_hello()


# def greeting(full_name: str) -> None:
#     """Function greets a person given full name as a string"""

#     print(f"Hello {full_name.split()[0]} {full_name.split()[1]}, How are you today?")

# greeting("John Doe")


# def greet_user(age: int) -> None:
#     eligible_to_enter = age > 21
#     if eligible_to_enter:
#         print("Welcome")
#     else:
#         print("Access denied")
