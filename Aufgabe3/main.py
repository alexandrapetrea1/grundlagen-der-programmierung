import random

alegere = ["foarfeca", "hartie", "piatra"]

sc = 0
sj = 0

for _ in range(3):
    calculator = random.choice(alegere)
    jucator = input("Jucatorul alege: ")
    if calculator == "foarfeca":
        if jucator == "hartie":
            sc = sc + 1
        if jucator == "piatra":
            sj = sj + 1
    if calculator == "hartie":
        if jucator == "foarfeca":
            sj = sj + 1
        if jucator == "piatra":
            sc = sc + 1
    if calculator == "piatra":
        if jucator == "foarfeca":
            sc = sc + 1
        if jucator == "hartie":
            sj = sj + 1
    print(f"Calculatorul a ales {calculator}, iar jucatorul a ales {jucator}. Scorul curent este {sc}-{sj}.")

if sc > sj:
    print("Calculatorul a castigat!")
else:
    print("Jucatorul a castigat!")

