import random



def GjetteSpill():
    maxTall = 100
    tilfeldigTall = random.randint(1, maxTall)
    antallGjett = 0
    loop = True

    while loop == True:
        brukerTall = input("Skriv inn tallet du vil tippe: ")
        brukerTall = int(brukerTall)

        if brukerTall == tilfeldigTall:
            print("Du gjettet riktig!")
            antallGjett += 1
            print("Antall gjett: " + str(antallGjett))
            loop = False

        if brukerTall > tilfeldigTall:
            print("Tallet du gjettet er for Høyt!")
            antallGjett += 1

        if brukerTall < tilfeldigTall:
            print("Tallet du gjettet er for Lavt!")
            antallGjett += 1

    if loop == False:
        restart = input("Vil du gjette på nytt? Skriv Ja eller Nei: ")
        restart = restart.upper()
        if restart == ("JA"):
            loop = True
            GjetteSpill()
        
        if restart == ("NEI"):
            print("Ok")
    
GjetteSpill()