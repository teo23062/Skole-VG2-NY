import random

TilfeldigTall = random.randint(1, 2000)

riktig = False

while riktig == False:
    Svar = input("Skriv ett tilfeldig tall her: ")
    Svar = int(Svar)

    if Svar == TilfeldigTall:
        print("Du gjettet riktig!")
        riktig = True
    elif Svar > TilfeldigTall:
        print("Du gjettet for Høyt!")
    elif Svar < TilfeldigTall:
        print("Du gjettet for Lavt!")
    
    if Svar > 0 and Svar < 500:
        print("Svaret er mellom 0 og 500")

    if Svar > 500 and Svar < 1000:
        print("Svaret er mellom 500 og 1000")

    if Svar > 1000 and Svar < 1500:
        print("Svaret er mellom 1000 og 1500")
    
    if Svar > 1500 and Svar < 2000:
        print("Svaret er mellom 1500 og 2000")

    input()

input()