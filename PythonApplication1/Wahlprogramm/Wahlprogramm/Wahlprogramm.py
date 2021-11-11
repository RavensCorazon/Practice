kan_1 = input("Geben Sie den Namen des ersten Kandidaten ein: ")
kan_2 = input("Geben Sie den Namen des zweiten Kandidaten ein: ")
kan_3 = input("Geben Sie den Namen des dritten Kandidaten ein: ")

St_1 = int(input(f"Geben Sie die Stimmenanzahl für {kan_1} ein: "))
St_2 = int(input(f"Geben Sie die Stimmenanzahl für {kan_2} ein: "))
St_3 = int(input(f"Geben Sie die Stimmenanzahl für {kan_3} ein: "))

all_St = St_1 + St_2 + St_3

all_kan1 = round(St_1 * 100 / float(all_St))
all_kan2 = round(St_2 * 100 / float(all_St))
all_kan3 = round(St_3 * 100 / float(all_St))

print(f"{kan_1} hat {all_kan1}% der Stimmen erhalten.")
print(f"{kan_2} hat {all_kan2}% der Stimmen erhalten.")
print(f"{kan_3} hat {all_kan3}% der Stimmen erhalten.")
