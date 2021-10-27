# brutto
brutto = float(input("Preis mit MwST eingeben: \n"))
preis = float(brutto) / 1.19
steuern = round(float(brutto) - float(preis))

print(f"Die MwST beträgt: {steuern}")
print(f"Der Nettobetrag ist {preis}\n\n")
# netto
netto = float(input("Preis ohne MwST eingeben: "))
steuern = float(netto) * 0.19
preis = float(netto) + float(steuern)

print(f"Die MwST beträgt: {steuern}")
print(f"Der Bruttobetrag ist {preis}")