# Create a variables containing strings for username and password. Start Endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print greeting message.


username = 'Ratamahata'
password = 'qwerty'

while True:
    if username == input('Enter username: ') and password == input('Enter password: '):
        print('Welcome, Ratamahata!')
        break
    print('Wrong username or password!')
    continue