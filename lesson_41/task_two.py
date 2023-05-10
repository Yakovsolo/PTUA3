"""ask Nr.2 : Write a User class that has a password property. 
The password property should be a computed property that checks whether the password 
is strong enough. A password is considered strong if it has at least 8 characters, 
contains at least one uppercase letter, one lowercase letter, and one number."""

import re

class User:
    def __init__(self) -> None:
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if not self.is_password_strong(value):
            raise ValueError("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.")
        self._password = value

    @staticmethod
    def is_password_strong(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        return True
        

new_user = User()

password = input("Input strong password:")
new_user.password = password
print(f'password: {new_user.password}')
            
# Output:
# old password: As523645
# Input strong password:Sa526892
# new password: Sa526892


# old password: As523645
# Input strong password:12345678
# ValueError: Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.

