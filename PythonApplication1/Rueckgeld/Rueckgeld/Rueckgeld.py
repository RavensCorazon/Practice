
artikel = float(input("Preis des Artikels: "))
kunde = float(input("Geld des Kunden: "))
rück = float(artikel) - float(kunde)

if kunde < artikel:
    print("Der Kunde hat zu wenig gezahlt.\n")
    kunde = float(input("Geld des Kunden: "))
elif kunde == artikel:
    print(rück)

print(f"\nDer Kunde bekommt {rück}€ zurück.")