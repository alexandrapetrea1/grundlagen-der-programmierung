from alfabet import *
from key_events import *
import turtle


def deseneaza_automat():
    cuvant = input("Dein Wort/Satz ist:")
    for caracter in cuvant:
        if caracter in al:
            al[caracter]()
        else:
            for ch in aln[caracter]:
                if ch == 'w':
                    draw_forward()
                if ch == 's':
                    draw_backward()
                if ch == 'd':
                    turn_right()
                if ch == 'a':
                    turn_left()
                if ch == 'f':
                    pick_up()
                if ch == 'g':
                    turn_down()


    turtle.done()

def deseneaza_manual():
    caracter_nou = input("neuer Charakter: ")
    with open ("keys_pressed.txt", "a") as file:
        file.write(f"{caracter_nou} : ")
    keys()
    turtle.listen()
    turtle.done()


def main():
    with open("keys_pressed.txt", "a") as file:
        file.write("\n")
    print('''
    Wahle:
    1-manuell zeichnen
    2-automatisch zeichnen

    ''')

    opt = int(input())
    if opt == 2:
        deseneaza_automat()
    else:
        if opt == 1:
            deseneaza_manual()
main()