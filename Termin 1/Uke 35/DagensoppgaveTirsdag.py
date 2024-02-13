import random 
# Lag et program som tar inn et tall fra brukeren. Programmet skal sjekke om tallet er positivt eller negativt. Hvis tallet er positivt, 
# skal programmet sjekke om tallet er større enn 100. Hvis tallet er negativt, skal programmet sjekke om tallet er mindre enn –100.
# Oppgave 1

Poengsum = input("Skriv din poengsum her: ")
Poengsum = int(Poengsum)

if Poengsum >= 90:
    print("Du fikk Karakter A")
elif Poengsum >= 80:
    print("Du fikk karakter B")
elif Poengsum >= 70:
    print("Du fikk karakter C")
elif Poengsum >= 60:
    print("Du fikk karakter D")
elif Poengsum < 60:
    print("Du fikk karakter F")
else:
    print("Pappa er rar")

# Lag en enkel kalkulator som tar inn to tall og en operator (+, -, *, /) som input fra brukeren. 
# Programmet skal deretter utføre den ønskede operasjonen og vise resultatet.
# Oppgave 2

tall1 = input("Skriv inn det førstetallet: ")
tall2 = input("Skriv inn det andre tallet: ")
Operator = input("Skriv inn en av operatorene (+, -, *, /): ")
tall1 = float(tall1)
tall2 = float(tall2)

print("Svaret ble: ")

if Operator == "+":
    print(tall1+tall2)
elif Operator == "-":
    print(tall1-tall2)
elif Operator == "*":
    print(tall1*tall2)
elif Operator == "/":
    print(tall1/tall2)
else:
    print("Hei på dei")

# Skriv et program som spør brukeren om hvilken time det er (på en 24-timers klokke) som input. Basert på tiden brukeren oppgir, 
# skal programmet gi en passende hilsen, for eksempel "God morgen!", "God ettermiddag!" eller "God kveld!".
# Oppgave 3

Klokken = input("Skriv inn hva tiden er (på en 24-timers klokke): ")
Klokken = int(Klokken)

if Klokken <= 6:
    print("God Natt!")
elif Klokken <= 12:
    print("God Morgen!")
elif Klokken <= 24:
    print("God Dag!")

# Skriv et program som tar inn et heltall som input. Programmet skal sjekke om tallet er et oddetall eller et partall, 
# og deretter gi passende tilbakemelding
# Oppgave 4

Tall3 = input("Skriv ditt tall her: ")
Tall3 = int(Tall3)

if Tall3 % 2 == 0:
    print("Tallet ditt er ett partall")
else:
    print("Tallet dit er ett oddetall")

# Skriv et program som ber brukeren om å oppgi et passord. Hvis passordet er "hemmelig", 
# skal programmet gi tilgang, ellers skal det nekte tilgang.
# Oppgave 5

Passord = "Hemmelig"
passordInput = input("Skriv inn passord her: ")

if passordInput == Passord:
    print("Du har fått tilgang!")
else:
    print("Du har blitt nektet tilgang")

# Lag et program som genererer et tilfeldig tall mellom 1 og 100. La brukeren gjette hvilket tall det er. 
# Gi hint om tallet er for høyt eller for lavt, og fortsett å la brukeren gjette til de gjetter riktig tall.
# Oppgave 6

tilfeldigTall = random.randint(0, 100)
gjetteTall = input("Skriv inn hva du gjetter: ")
gjetteTall = int(gjetteTall)

if gjetteTall == tilfeldigTall:
    print("Du gjettet riktig!")
else:
    print("Du gjettet feil!")