# https://cataas.com/cat kas kartą užkrauna vis skirtingą katės nuotrauką. Parašykite funkciją, kuriai į parametrus
# įrašius, kiek norime nuotraukų, išsaugotų jas mūsų kompiuteryje.

import requests


def get_cats_photo(quantity: int):
    for photos in range(1, quantity + 1):
        r = requests.get("https://cataas.com/cat")
        with open(f"cat {photos}.png", "wb") as f:
            f.write(r.content)


get_cats_photo(5)
