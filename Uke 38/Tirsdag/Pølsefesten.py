import math # Importerer math siden ejg trenger det senere

AntallOstepolse = input("Hvor mange skal ha ostepølse?: ") # Ber brukerern om å skrive hvor mange som skal ha ostepølse
AntallGrillpolser = input("Hvor mange skal ha grillpølse: ") # Ber brukeren om å skrive hvor mange som skal ha grillpølse
Polserperpers = input("Hvor mange pølser skal hver person spise?: ") # Spørr brukerer om hvor mange pølser hver person spiser

AntallOstepolse = int(AntallOstepolse) # Runner tallet ned til nærmeste heltall slik at brukeren ikke kan skrive desimaltall
AntallGrillpolser = int(AntallGrillpolser) # Runner tallet ned til nærmeste heltall slik at brukeren ikke kan skrive desimaltall
Polserperpers = int(Polserperpers) # Runner tallet ned til nærmeste heltall slik at brukeren ikke kan skrive desimaltall

Ostepolsepakke = 6 # Sier hvor mange ostepølser det er i hver pakke
Grillpolsepakke = 10 # Sider hvor mange grill pølser det er i en pakke
Polsebrodipakke = 8 # Sier hvor mange pølsebrød det er i en pakke

def Polseregner(): # Lager en pølsergener funkjson
    antallostepols = AntallOstepolse * Polserperpers # Finenr ut av hvor mange pølser det til sammen blir
    antallgrillpols = AntallGrillpolser * Polserperpers # Finenr ut av hvor mange pølser det til sammen blir

    totalpolser = antallgrillpols + antallostepols # Regner ut total antall pølser

    Antallpakkerostepols = math.ceil(antallostepols / Ostepolsepakke) # Runder av til nærmeste heltall slik at du ikke trenger å kjøpe deismaltall
    Antallpakkergrillpols = math.ceil(antallgrillpols / Grillpolsepakke) # Runder av til nærmeste heltall slik at du ikke trenger å kjøpe deismaltall
    Antallbrødpakker = math.ceil(totalpolser / Polsebrodipakke) # Runder av til nærmeste heltall slik at du ikke trenger å kjøpe deismaltall

    OstePolserTilOvers = (Antallpakkerostepols * Ostepolsepakke) - antallostepols # Regner ut hvor mange pølser det blir til overs
    Grillpolstilovers = (Antallpakkergrillpols * Grillpolsepakke) - antallgrillpols # Regner ut hvor mange pølser det blir til overs
    PolsebrodTilOvers = (Antallbrødpakker * Polsebrodipakke) - totalpolser # Regner hvor mange pølsebrød det blir til overs

    print("Du trenger " + str(int(Antallpakkerostepols)) + " ostepølsepakker til festen") # Printer antall ostepølsepakker
    print("Du trenger " + str(int(Antallpakkergrillpols)) + " grillpølsepakker til festen") # Printer antall grillpølsepakker
    print("Du trenger " + str(int(Antallbrødpakker)) + " pølsebrød pakke til festen") # Printer antall pølsebrød pakker

    print("Det er " + str(int(OstePolserTilOvers)) + " ostepølser til overs") # Printer antall ostepølser til overs
    print("Det er " + str(int(Grillpolstilovers)) + " grillpølser til overs") # Printer antall grillpølser til overs
    print("Det er " + str(int(PolsebrodTilOvers)) + " pølsebrød til overs") # Printer antall pølsebrød til overs
Polseregner() # kaller på pølseregner funksjonen
input()