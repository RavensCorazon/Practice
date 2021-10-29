a = float(input("Länge eingeben: "))

if a < 0:
    print("Sie haben eine Negative Zahl eingegeben. Bitte eine richtige Zahl eingeben\n")
    a = float(input("Länge eingeben: "))
elif a == 1:
    print(a)

b = float(input("Breite eingeben: "))

if b < 0:
    print("Sie haben eine Negative Zahl eingegeben. Bitte eine richtige Zahl eingeben\n")
    b = float(input("Breite eingeben: "))
elif a == 1:
    print(b)

c = float(input("Höhe eingeben: "))

if c < 0:
    print("Sie haben eine Negative Zahl eingegeben. Bitte eine richtige Zahl eingeben\n")
    c = float(input("Höhe eingeben: "))
elif a == 1:
    print(c)

ober = 2 * float(a) * float(b) + 2 * float(a) * float(c) + 2 * float(b) * float(c)
ergebnis = float(ober)
print(f"Die Oberfläche des Quader beträgt: {ergebnis}")