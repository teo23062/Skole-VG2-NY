Spoersmaal = ["Er ost godt?", "Hvilken skole går vi på?", "Er himmelen blå?", "Hvor mange cc kan en lettmc ha?", "Er python enkelt?", "Er sand blå?",] # Lage en liste med alle spørsmålene

Alternativ1 = ["Kanskje", "Skogmo VGS", "Ja", "75cc", "Aldri i verden", "Den er grønn"] # Lage en liste med alternativ 1
Alternativ2 = ["Nei", "Porgsrunn VGS", "Nei", "125cc", "Hvorfor ikke", "Ja"] # Lage en liste med alternativ 2
Alternativ3 = ["Ja", "Skien VGS", "Den er gul", "200cc", "Ja", "Nei"] # lage en liste med alternativ 3
riktigSvar = [3, 2, 1, 2, 1, 1] #Riktig svar

peongsum = 0 # Lage en variabel som holder brukerens peongsum

for i in range(len(Spoersmaal)): # Lage en for løkke som skal gå gjennom alle spørsmålene å printe de
    print(Spoersmaal[i]) #Printer spørsmålene
    print("Dette er dine svarsalternativ: ", Alternativ1[i], ",", Alternativ2[i], "Eller", Alternativ3[i]) # Printer spørsmålene i riktig rekkefølge
    brukerSvar = input("Skriv inn alternativ 1, 2 eller 3: ") # Spør etter svar

if brukerSvar.isnumeric():# Sjekker om brukeren skriver riktig svar
    if int(brukerSvar) == riktigSvar[i]:
        print("Riktig!")
        peongsum += 1
    else:
        print("Feil")        
    print("------------------------------------")
else:
    print("Ikke ett gyldig svar")
