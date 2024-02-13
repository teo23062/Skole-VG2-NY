#Her så lager jeg både en maanednr input som henter månednummer brukeren skriver og maanednrer som sier hvilken måned det er. 
maanednr = input("Oppgi nummeret til måneden vi er i ")
maanednrer = 8
maanednrer = int(maanednrer)
maanednr = int(maanednr)


if maanednr == maanednrer:
  print("Du skrev riktig måned!")

elif maanednr >= 1 and maanednr <= 12:
  print(f"Du skrev ikke inn rikitg måned, du skrev: {maanednr}")
else:
  print("Du må oppgi et tall mellom 1 og 12.")