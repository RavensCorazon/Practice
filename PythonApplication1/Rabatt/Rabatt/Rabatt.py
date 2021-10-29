preis = float(input(f"Bitte geben Sie den Preis an der Rabatt bekommen soll: "))
rabatt_prozent = float(input(f"Geben Sie den Rabatt ein: "))

if rabatt_prozent > 99.99:
    print("Mehr als 100% Rabatt nicht möglich.\n")
    rabatt_prozent = float(input(f"Geben Sie den Rabatt ein: "))
elif rabatt_prozent == 1:
    print(rabatt_prozent)

rabatt = float(preis) * float(rabatt_prozent) / 100
Endpreis = float(preis) - float(rabatt)

print(f"Das ist der Startpreis: {preis}")
print(f"Darauf gibt es {rabatt_prozent}%, dies sind {rabatt}€")
print(f"Der Endpreis beträgt: {Endpreis}")
