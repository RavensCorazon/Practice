# netto
netto = float(input("Preis ohne MwST eingeben: "))
steuern = float(netto) * 0.19
preis = float(netto) + float(steuern)

print(f"Die MwST beträgt: {steuern}")
print(f"Der Bruttobetrag ist {preis}")