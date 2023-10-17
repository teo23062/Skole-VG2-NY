import random # Importere random

Hvorlang = input("Hvor lang skal koden være?: ") #Spørre brukeren om hvor langt passordet skal være
Hvorlang = int(Hvorlang) # Gjøre det om til en int

Passord = [] # Lage en liste som lagrer passordet som blir generert

for i in range(Hvorlang): # Kjører antall ganger som brukeren definerer
    
    tall = random.randint(0,9) # Genererer tilfeldig tall
    Passord += str(tall) # Putte tallet inni passord listen

print(Passord) # Printe passordet