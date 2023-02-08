# Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

vip_list = ['Algirdas', 'Petras', 'Jurgis']

name = input('Enter yourn name: ')
if name in vip_list:
    print(f'Dear {name}, we are glad to see you here!')
else:
    print(f'Who is {name}? Get outta here!')