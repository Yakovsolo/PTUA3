# Parašyti programą, kuri:

# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17

# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

import datetime

x = datetime.datetime.today()
print(x)
print(x + datetime.timedelta(hours=8))
print(x.strftime("%Y %m %d %H:%M:%S"))
