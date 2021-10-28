kapital = float(input("Bitte geben Sie ihr Startkapital ein: "))
zinssatz = float(input("Geben Sie hier ihren Zinssatz ein: "))
zinsen = float(kapital) * float(zinssatz) / 100

print(f"\nIhr Startkapital beträgt: {kapital}")
print(f"Ihr Angegebener Zinssatz beträgt {zinssatz}%")
print(f"Ihre Jahreszinsen betragen: {zinsen}")

