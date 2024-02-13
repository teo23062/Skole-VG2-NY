Passordet = input("Hva er passordet du vil sjekke?: ") # Spørre om hva passordet er

lagntnok = False # Ikke lang nok
Minstetttall = False # Ikke noe tall
Minstettspesialtegn = False # Ikke noe spesial tegn
StoreBokstaver = False # Ikke noe stor bokstav
SmaaBokstaver = False # Ikke noe små bokstav

if len(Passordet) >= 8: # Sjekker lengden på passordet om det er større en 8
    lagntnok = True # Sier at den er lang nok

for i in range(0, len(Passordet)): # Kjører en gang for hver bokstav 
    if Passordet[i].isupper(): # Sjekker om bokstaven er stor
        StoreBokstaver = True # Sier at passordet har en stor bokstav
    elif Passordet[i].islower(): # Sjekker om bokstaven er liten
        SmaaBokstaver = True # Sier at passordet har en liten bokstav
    elif Passordet[i].isnumeric(): # Sjekker om passordet har tall
        Minstetttall = True # Sier at passordet har ett tall
    else: # Ellers
        Minstettspesialtegn = True # Sier at passordet har ett spesialtegn

if lagntnok == False: print("Du burde ha minst 8 tegn") # Hvis du ikke har lagnt nok så ber den deg om å endre
if SmaaBokstaver == False: print("Legg til en liten bokstav") # Hvis du ikke har liten bokstav så ber den deg om å endre
if StoreBokstaver == False: print("Legg til en stor bokstav") # Hvis du ikke har stor bokstav så ber den deg om å endre
if Minstettspesialtegn == False: print("Legg til ett spesialtegn") # Hvis du ikke har spesialtegn så ber den deg om å endre
if Minstetttall == False: print("Legg til ett tall") # Hvis du ikke har ett tall så ber den deg om å endre

if lagntnok and SmaaBokstaver and StoreBokstaver and Minstettspesialtegn and Minstetttall: # Hvis alle er True
    print("Passordet oppfyller alle kravene.") # Sier til brukeren at du fyller alle kravene og at passordet er bra
