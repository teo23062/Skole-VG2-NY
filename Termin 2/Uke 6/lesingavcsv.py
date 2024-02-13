import pandas as pd
from tkinter import *
from tkinter import ttk

file_path = r"C:\Users\teo23062\OneDrive - Vestfold og Telemark fylkeskommune\Skole VG2\Utvikling VG2\Uke 6\ansatte.csv"
df = pd.read_csv(file_path)

# Oppgave 1
antall_kjonn = df['kjonn'].value_counts()

print("Antall menn:", antall_kjonn['mann'])
print("Antall kvinner:", antall_kjonn['kvinne'])

# Oppgave 2
gjennomsnittlonn_alle = df['lonn'].mean()

print("Total lønn: ", gjennomsnittlonn_alle)

# Opphave 3
kvinner_df = df[df['kjonn'] == 'kvinne']
gjennomsnittfor_kvinner = kvinner_df['lonn'].mean()

print("Gjennomsnitt for kvinner: ", gjennomsnittfor_kvinner)

# Oppgave 4
menn_df = df[df['kjonn'] == 'mann']
gjennomsnittfor_menn = menn_df['lonn'].mean()

print("Gjennomsnitt for menn: ", gjennomsnittfor_menn)

# Oppgave 5
kvinner_df = df[df['kjonn'] == 'kvinne']

kvinner_df_sorted = kvinner_df.sort_values(by='lonn', ascending=False)
kvinner_df_sorted1 = kvinner_df.sort_values(by='lonn')

hoyest_lonn_kvinne = kvinner_df_sorted.iloc[0]
laveste_lonn_kvinne = kvinner_df_sorted1.iloc[0]

print("Kvinne med høyest lønn:")
print(hoyest_lonn_kvinne)

print("Kvinne med lavest lønn:")
print(laveste_lonn_kvinne)

# Oppgave 6
Navndagnavn = ['Dora','Dorte','Dortea']

for i in Navndagnavn:
    Navnedag_df = df[df['fornavn'] == i]
    print("Name:", i)
    print("Found rows:", Navnedag_df)  # Check if any rows are found

# Oppgave 7
Avdelinger = ['ledelsen','salg','teknisk','regnskap']

for i in Avdelinger:
    avdeling_df = df[df['avdeling'] == i]
    totallonn_for_avdelinger = avdeling_df['lonn'].mean()

    print("Name:", i)
    print("Total lønn",totallonn_for_avdelinger)

# Oppgave 8
sorted_df = df.sort_values(by='etternavn')

print(sorted_df)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()