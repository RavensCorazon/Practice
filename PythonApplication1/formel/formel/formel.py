import math

def formel(a, b, c):

    disc = (-b**2) - 4 * a * c

    x1 = (-b - math.sqrt(abs(disc))) / (2 * a)
    x2 = (-b + math.sqrt(abs(disc))) / (2 * a)
    
    if disc < 0:
        print(f"Zwei Möglichkeiten: {x1} und {x2}")
        
    elif disc == 0:
        print("Eine Lösung: ")
        print(-b / (2*a))
        
    else:
        print("Zwei andere Lösungen: ")
        print(- b / (2 * a), " + i", x2)
        print(- b / (2 * a), " - i", x1)
    

a = int(input("Geben Sie die erste Zahl ein: "))
b = int(input("Geben sie eine zweite Zahl ein: "))
c = int(input("Geben Sie eine dritte Zahl ein: "))    

if a == 0:
    print("Falsche Eingabe")
else:
    formel(a, b, c)