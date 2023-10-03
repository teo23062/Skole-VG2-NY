import math

betalingsSum = input("Skriv inn hvor mye du må betale: ")
betalermedHva = input("Skriv inn hva du betaler med (100, 200, 500 eller 1000 seddel: ")
betalingsSum = int(betalingsSum)
betalermedHva = int(betalermedHva)

if betalingsSum >= 1000:
    print("Du får tilbake: " + str(math.floor(betalermedHva/1000)) + " Tusenseddler")
    betalingsSum %= 1000

if betalingsSum >= 500:
    print("Du får tilbake: " + str(math.floor(betalermedHva/500)) + " Femhundreseddler")
    betalingsSum %= 500

if betalingsSum >= 200:
    print("Du får tilbake: " + str(math.floor(betalermedHva/200)) + " Tohundreseddler")
    betalingsSum %= 200

if betalingsSum >= 100:
    print("Du får tilbake: " + str(math.floor(betalermedHva/100)) + " Hundreseddler")
    betalingsSum %= 100

if betalingsSum >= 50:
    print("Du får tilbake: " + str(math.floor(betalermedHva/50)) + " Femtiseddler")
    betalingsSum %= 50

if betalingsSum >= 20:
    print("Du får tilbake: " + str(math.floor(betalermedHva/20)) + " Tjuekroning")
    betalingsSum %= 20

if betalingsSum >= 10:
    print("Du får tilbake: " + str(math.floor(betalermedHva/10)) + " Tikroning")
    betalingsSum %= 10

if betalingsSum >= 1:
    print("Du får tilbake: " + str(math.floor(betalermedHva/1)) + " Enkroning")
    betalingsSum %= 1