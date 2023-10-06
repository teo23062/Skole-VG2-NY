Lengde = 297 # Definerer lengden på ett A4 ark
Bredde = 210 # Definerer bredden på ett A4 ark

hoyde = 0 # Høyden til arket er definert som 0 i starten og blir høyerer etterhver

MaksHoyde = 0 # Maks Volumet den kommer fram til
NoverendeHoyde = 0 # Det volumet den foreløpig har kommet fram til

while NoverendeHoyde == MaksHoyde: # Sier det at så lenge NoverendeHoyde og MaksHoyde er likt så skal den kjøre
    vLengde = Lengde - (hoyde*2) # Regner ut Lengden på A4 arket etter at den har brettet sidene
    vBredde = Bredde - (hoyde*2) # Regner ut bredden på A4 arket etter at den har brettet sidene

    NoverendeHoyde = (vBredde * vLengde * hoyde) / 1000000 # Regner ut Volumet i Liter

    print("Utregnet volum: " + str(NoverendeHoyde)) # Printer ut Noverende høyde slik at vi kan se hva den kommer fram til

    if NoverendeHoyde > MaksHoyde: # Sier at hvis noverende høyde er større en maks høyde så skal den kjøre
        MaksHoyde = NoverendeHoyde # Sier at MaksHoyde er det samme som NoverendeHoyde
    
    hoyde += 1 # Legger til 1 på hoyden slik at den regner høyere

print("Maksimal høyde for optimalt volum er: " + str(MaksHoyde)) # Printer ut sluttresultatet
