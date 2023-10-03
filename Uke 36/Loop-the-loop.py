#Her så printer vi ut alle tallene fra 0-99
for i in range(100):
    print(i)

#Her så teller vi ned fra 99 til 0
for i in range(99, 0, -1):
    print(i)

#Her så teller vi opp til 98 men vi plusser på to
for i in range(0, 98, 2):
    print(i)

#Nå skal vi printe ut 5 gangen opp til hundre
for i in range(0, 101, 5):
    print(i)

#Nå skal vi printe ut 5 gangen men vi starter på -50 og slutter på 50
for i in range(-50, 50, 5):
    print(i)

#Nå skal vi printe ut all partall
for i in range(1, 101, 2):
    print(i)


antall = input("Skriv antall ganger her: ") #Lager en inpit der brukeren kan skrive antall ganger den skal kjøre
antall = int(antall) #Gjør det om til en int

for i in range(1, antall + 1): # Her så henter vi hvor mange gange den skal kjøre fra antall variabelen over så bruker vi den og plusser på en for hver gang den skal kjøre
    print("*" * i) #printer stjerner


n = 5 #Antall linjer
for i in range(n): #Henter antall linjer
    if i % 2 == 0: 
        print('*' * 4) #Printer stjerner
    else:
        print('*')