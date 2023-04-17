import pickle

# a = 1024

# with open("a.pkl", "wb") as pickle_out:
#     pickle.dump(a, pickle_out)

# with open("a.pkl", "rb") as pickle_in:
#     naujas_a = pickle.load(pickle_in)

# print(naujas_a)


# a = 10
# b = 7
# c = 23

# with open("abc.pkl", "wb") as pickle_out:
#     pickle.dump(a, pickle_out)
#     pickle.dump(b, pickle_out)
#     pickle.dump(c, pickle_out)

# with open("abc.pkl", "rb") as pickle_in:
#     while True:
#         try:
#             print(pickle.load(pickle_in))
#         except EOFError:
#             break

# with open("abc.pkl", "rb") as pickle_in:
#     nauja_a = pickle.load(pickle_in)
#     nauja_b = pickle.load(pickle_in)
#     nauja_c = pickle.load(pickle_in)

# print(nauja_a)
# print(nauja_b)
# print(nauja_c)

# 10
# 7
# 23

import pickle


class Automobilis:
    def __init__(self, marke, modelis):
        self.marke = marke
        self.modelis = modelis


automobiliai = [
    Automobilis("Toyota", "Avensis"),
    Automobilis("Toyota", "Corolla"),
    Automobilis("Toyota", "Camry"),
]

with open("automobilis.pkl", "wb") as failas:
    pickle.dump(automobiliai, failas)

with open("automobilis.pkl", "rb") as failas:
    automobiliai = pickle.load(failas)
    for automobilis in automobiliai:
        print("Markė", automobilis.marke)
        print("Modelis", automobilis.modelis)
