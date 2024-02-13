import random 

print("Oppgave 1, 2 og 3")
# I dette eksempelet så bruker jeg fornavn som en variabel med stringen Teodor.
fornavn = "Teodor"

# Så printer jeg ut forksjellige tekster med print("") og legger til tekst og variabelen fornavn=("")
print("Halla " + fornavn + "!")
print("Hvordan har du det " + fornavn + "?")
print("Skal du kjøre masse i dag " + fornavn + "?")

#-------------------------------------------------------------------------
print("Oppgave 5 og 4")

# Her lager vi en variabel med navn a og gir den verdien 7 så printer vi a
a = 7
print(a)

# Her endrer vi variabelen a til a = a + 1 som betyr at verdien endres til 8
# Det samme gjør vi med b, da sier vi at b er a - 2 som betyr at den blir 6 så printer vi ut begge
a = a + 1
b = a - 2

print(a)
print(b)

#------------------------------------------------------------------------
# Det som er galt med denne koden antall biletter = 4 er det at du skal ha sammensatt der det første ordet skal ha en liten forbokstav
# og den andre skal ha stor altså antallBiletter = 4

# Det som er feil med andel = 52,5 er det at man ikke kan bruke , men sitedetfor .

# Det som er feil med denne koden 1.premie = 1000 er det at du ikke kan ha . i variabel navnet, så da må det bli 1Premie = 1000

#------------------------------------------------------------------------
print("Oppgave 7")
# Her så printer vi ut forskjellige regnestykker som Python regner ut.

print(3+2*3)
print(2**3-8/2)
print(3*4/2)

#------------------------------------------------------------------------
#print("Oppgave 9")

#print(6 / 2 (1 + 2))

#------------------------------------------------------------------------
print("Oppgave 11")



tall = random.randint(1, 2)
Navn = ["Teodor", "Oliver"]

if len(Navn) >= 3:
    element = Navn[2]
else:
    element = None

first_element = Navn[0]
second_element = Navn[1]

if tall > 1:
    print(first_element)
    print(tall)
else:
    print(second_element)
    print(tall)



