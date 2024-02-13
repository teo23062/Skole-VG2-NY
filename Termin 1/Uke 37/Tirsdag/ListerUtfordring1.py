Heltall = [7, 1, 6, 3, 4, 2, 6, 3, 5, 9, 9, 3, 4, 7, 1, 6, 3, 7, 8, 4, 8, 5 ,1 ,2]

enere = 0
toere = 0
treere = 0
firrere = 0
femmere = 0
seksere = 0
syvere = 0
ottere = 0
niere = 0

for x in Heltall:
  if x == 1:
    enere = enere + 1
  if x == 2:
    toere = toere + 1
  if x == 3:
    treere = treere + 1
  if x == 4:
    firrere = firrere + 1
  if x == 5:
    femmere = femmere + 1
  if x == 6:
    seksere = seksere + 1
  if x == 7:
    syvere = syvere + 1
  if x == 8:
    ottere = ottere + 1
  if x == 9:
    niere = niere + 1

print(f"Enere: {enere}, Toere: {toere}, Treere: {treere}, Forrere: {firrere}, Femmere: {femmere}, Seksere: {seksere}, Syvere: {syvere}, Åttere: {ottere}, Niere: {niere},")
