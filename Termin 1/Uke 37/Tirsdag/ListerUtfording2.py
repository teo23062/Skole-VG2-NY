Ord = ["F", "R", "I", "K"] # Lager en array med ett ord

def spill():
    gjettOrd = ["-", "-", "-", "-"] # Lager en variabel som skal lagre om du har skrevet inn riktig bokstav
    vunnet = False # Sier at du ikke har vunnet

    while not vunnet: # Sier det at når du ikke har vunnet så skal denne kjøre
        Bokstav = input("Skriv bokstav her: ") # Lager en input felt der brukeren kan gjette bokstav

        for i in range(len(Ord)): # Henter lengden på Ordet som i dette tilfellet er Frik
            if Ord[i] == Bokstav.upper(): # Så sier den at hvis bokstaven du gjetter er en av de i Ordet så skal den kjøre print
                gjettOrd[i] = Bokstav.upper() # Lagrer bokstaven i Variabelen som heter gjettOrd
        if Ord == gjettOrd: # Sier at hvis Ord er det samme som gjettOrd så skal den kjøre det under
            print("Du har vunnet!") # Printer du har vunnet
            vunnet = True # Sier at du har vunnet 
        print(gjettOrd) # Printer Gjettord som viser - - - - i konsollen

    while vunnet != False:    # Sjekke at hvis vunnet er satt til true så skal den gjøre det under    
        JellerN = input("Vil du gjette igjen? J for ja N for nei: ") # Spørre bruker om de vil gjette på nytt
        if JellerN.upper() == "J": # Hvis brukeren sier J for Ja så skal den gjøre det under
            vunnet = False # Setter vunnet til false
            gjettOrd = ["-", "-", "-", "-"] # Resetter bokstaver gjettet
            spill() # Kjører spillet på nytt 
        elif JellerN.upper() == "N": # Hvis bruker taster N så skal den gjøre det under
            break # Stopper programmet
        break # Stopper programmet
spill() # Kjører spillet på starten