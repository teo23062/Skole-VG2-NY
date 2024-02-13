# Skriv et program som sjekker om et tall som skrives inn av brukeren, er positivt, negativt eller 0.
# Oppgave 1


tall = input("Skriv tall her:")
tall = int(tall)

if tall > 0:
    print("Tallet er positivt")

elif tall < 0:
    print("Tallet er negativt")

else:
    print("Tallet er null")


# Du skal lage et program som tar inn et tall fra brukeren og sjekker om tallet er énsifret 
# (0–9), tosifret (10–99), tresifret (100–999), firesifret (1000–9999) eller mer enn firesifret (10000+).
# Oppgave 2

tall2 = input("Skriv tall her:")
tall2 = int(tall2)

if tall2 < 0:
    print("Tallet er negativt")
elif tall2 <= 9:
    print("Tallet er ensifret")
elif tall2 <= 99:
    print("Tallet er tosifret")
elif tall2 <= 999:
    print("Tallet er tresifret")
elif tall2 <= 9999:
    print("Tallet er firesifret")
else:
    print("Tallet er større en firesifer")

# Skriv et program som sjekker om et tall som skrives inn av brukeren, ligger mellom 50 og 100. Denne oppgaven må du løse med to if -setninger. 
# Vi skal snart se hvordan vi kan løse den på en enklere måte.
# Oppgave 3

tall3 = input("Skriv tallet her:")
tall3 = int(tall3)

if tall3 > 50 & tall3 < 100:
    print("Tallet er mellom 50 og 100")
else:
    print("Tallet er ikke mellom 50 og hundre")

# På oppgave 4 så er feilen det at den sjekker om temperaturen er over 0 og den vil alltid være det så da er vannet i flytende form, man burde bytte plassene slik
# at den sjekker om den er over 100 og hvis den ikke er det så sjekker den om den er over 0.


# Lag et program som tar inn et tall fra brukeren. Programmet skal sjekke om tallet er positivt eller negativt. Hvis tallet er positivt, 
# skal programmet sjekke om tallet er større enn 100. Hvis tallet er negativt, skal programmet sjekke om tallet er mindre enn –100.
# Oppgave 5

tall4 = input("Skriv tallet her:")
tallverdi = int
tall4 = int(tall4)

if tall4 > 0:
    print("Tallet er positivt")
    if tall4 > 100:
        print("Tallet er over 100")
elif tall4 < 0:
    print("Tallet er negativt")
    if tall4 < -100:
        print("Tallet er mindre enn -100")
else:
    print("Tallet er 0")