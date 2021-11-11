prop_len = float(input("Geben Sie die Grundstückslänge ein: "))
prop_wid = float(input("Geben Sie die Gründstücksbreite ein: "))
prop_qm = float(input("Geben Sie den Preis pro Quadratmeter ein: "))
m_prov = input("Geben Sie die Maklerprovision in % an: ")
ust = input("Geben Sie die aktuelle Umsatzsteuer an: ")

prop = prop_len * prop_wid
prop_val = round(prop * prop_qm / 1)

m_hval = prop_val * 2 / 100
ust_m = m_hval * 19 / 100
m_val = m_hval + ust_m

print(f"Die Maklerprovision beträgt {m_val}€ und der Gründstückspreis beträgt {prop_val}€.")