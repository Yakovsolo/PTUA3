countries_and_capitals = {
    'Lithuania': 'Vilnius',
    'Poland': 'Warszaw',
    'Latvia': {
        'capital': 'Riga',
        'population': 2000000,
        'rich': 'poor'
    }
}
# print(countries_and_capitals['Latvia']['capital'] )
# print(countries_and_capitals.get('Latvia').get('population'))

# print(countries_and_capitals.items())

# print(list(countries_and_capitals.items()))

# print(countries_and_capitals.keys())

# # !!!   Kurti kopija jei ne reikia keisti zodyno

# countries_and_capitals.pop('Latvia')
# # print(countries_and_capitals)

# new_country = {'Spain': 'Madrid', 'France': 'Paris'}
# countries_and_capitals.update(new_country)
# print(countries_and_capitals)

test_keys = ['Albert', 'Tom', 'Stephen', 'Aurius']
test_values = [1, 4, 5]
my_dictionary = dict(zip(test_keys, test_values))
print(my_dictionary)
