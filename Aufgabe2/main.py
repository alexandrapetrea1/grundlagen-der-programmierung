intrare = open("intrare.txt", "r")
iesire = open("iesire.txt", "w")

cuv1 = input("cuvant de inlocuit: ")
cuv2 = input("cuvant de inlocuire: ")

cuvinte = intrare.read().split()
sir = ""
cnt = 0
for cuv in cuvinte:
    if cuv == cuv1:
        sir = sir + cuv2
        cnt = cnt + 1
    else:
        sir = sir + cuv
    sir = sir + " "
iesire.write(sir)

if cnt == 0:
    print("Nu s-a produs nicio inlocuire.")
else:
    print(f"{cuv1} a fost inlocuit cu {cuv2} de {cnt} ori.")
