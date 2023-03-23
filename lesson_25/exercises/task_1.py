# Task Nr.1:
# Create .env file with environmental variables:

# username
# password
# Write an application asking user to enter username and password. Check if user entered the same credentials as in
# your .env file. If so print "ACCESS GRANTED" Otherwise print "WRONG CREDENTIALS" until user enters correct details.

from dotenv import dotenv_values


def check_access() -> None:
    username = input("Enter username:\n")
    password = input("Enter your password:\n")
    check_dict = dotenv_values(".env")
    if username == check_dict["USERNAME"]:
        if password == check_dict["PASSWORD"]:
            print("ACCESS GRANTED")

    else:
        print("WRONG CREDENTIALS")
        return check_access()


check_access()
