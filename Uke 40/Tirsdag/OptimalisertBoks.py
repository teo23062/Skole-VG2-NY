Lengde = 297
Bredde = 210

hoyde = 0

MaksHoyde = 0
NoverendeHoyde = 0

while NoverendeHoyde == MaksHoyde:
    vLengde = Lengde - (hoyde*2)
    vBredde = Bredde - (hoyde*2)

    NoverendeHoyde = (vBredde * vLengde * hoyde) / 1000000

    print("Utregnet volum: " + str(NoverendeHoyde))

    if NoverendeHoyde > MaksHoyde:
        MaksHoyde = NoverendeHoyde
    
    hoyde += 1

print("Maksimal høyde for optimalt volum er: " + str(MaksHoyde))
