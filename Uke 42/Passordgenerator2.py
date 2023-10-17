import random # Importere random

Hvorlang = input("Hvor lang skal koden være?: ") # Spørre brukeren om hvor langt passordet skal være
Hvorlang = int(Hvorlang) # Gjøre det om til en int

Passord = "" # Lage en liste som lagrer passordet som blir generert

for i in range(Hvorlang): # Kjører antall ganger som brukeren definerer
    
    asciiTegn = chr(random.randint(33, 126)) # Generere tilfeldig ascii tegn mellom 33 og 126 

    Passord += str(asciiTegn) # Putte de tegnene generert inni passord variabelen

print(Passord) # Printe passordet