text = input("Input your text: ")
translation_table = {
    "A":"∆",
    "B": "8",
    "C":"<",
    "D":"|)",
    "E":"3",
    "F":"7",
    "G":"9",
    "H":"|-|",
    "I":"!",
    "J":"√",
    "K":"|<",
    "L":"|_",
    "M":"|\/|",
    "N":"/V",
    "O":"Ø",
    "P":"/o",
    "Q":"(,)",
    "R":"|2",
    "S":"5",
    "T":"7",
    "U":"|_|",
    "V":"\/",
    "W":"\/\/",
    "X":"><",
    "Y":"`/",
    "Z":"7_",
    "a": ""
}
leet_speek = text.replace_multi("A", "∆")
print(leet_speek)