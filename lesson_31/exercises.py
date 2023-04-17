# Sukurti programą, kuri:

# Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
# Atspausdintų tekstą iš sukurto failo
# Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
# Atspausdintų visą failo tekstą atbulai
# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

from this import d, s
from datetime import datetime

x = "".join([d.get(c, c) for c in s])


with open("text.txt", "w") as f:
    f.write(x)

with open("text.txt", "r") as f:
    sentence = f.read()
    print(sentence)

with open("text.txt", "a") as f:
    f.write("\n" + str(datetime.today()))

with open("text.txt", "+a") as f:
    lines = f.readlines()
    for index, line in enumerate(lines, start=1):
        f.write(f"{index}. {line}")
        # print(f"{index}. {line}")
