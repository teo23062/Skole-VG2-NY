Lengde = 297
Bredde = 210
Hoyde = 1

Optimalisering = False
MaksHoyde = 0
NoverendeHoyde = 0

while not Optimalisering:
    NoverendeHoyde = (Bredde - (Hoyde * 2)) * (Lengde - (Hoyde * 2)) * Hoyde / 1000000

    if NoverendeHoyde > MaksHoyde:
        MaksHoyde = NoverendeHoyde

    Hoyde += 0.1

    if NoverendeHoyde <= MaksHoyde:
        Optimalisering = True

print("Maksimal høyde for optimalt volum er: " + str(MaksHoyde))
