zinsen = float(input("Bitte geben Sie hier Ihr Jahreszinsen ein: "))
zinssatz = float(input("Bitte geben Sie hier Ihren Zinssatz ein: "))
kapital = float(zinsen) * 100 / float(zinssatz)

print(f"\nIhre Jahreszinsen sind: {zinsen}")
print(f"Ihr Angegebener Zinssatz beträgt {zinssatz}%")
print(f"Ihr Kapital beträgt: {kapital}")
