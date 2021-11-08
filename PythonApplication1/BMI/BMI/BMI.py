
def bmi_M():
    if  bmi < 20:
       print(f"Sie haben ein BMI von {bmi} und haben Untergewicht")
    elif bmi < 25:
        print(f"Sie haben ein BMI von {bmi} und sind Normalgewichtig")
    elif bmi < 30:
       print(f"Sie haben ein BMI von {bmi} und sind Übergewichtig")
    elif bmi < 34:
       print(f"Sie haben ein BMI von {bmi} und sind stark Übergewichtig.")
    elif bmi < 39:
       print(f"Sie haben ein BMI von {bmi} und haben Adipositas Grad II.")
    elif bmi > 40:
      print(f"Sie haben ein BMI von {bmi} und haben Adipositas Grad III.")


def bmi_W():
    if  bmi < 19:
       print(f"Sie haben ein BMI von {bmi} und haben Untergewicht")
    elif bmi < 23:
        print(f"Sie haben ein BMI von {bmi} und sind Normalgewichtig")
    elif bmi < 29:
       print(f"Sie haben ein BMI von {bmi} und sind Übergewichtig")
    elif bmi < 34:
       print(f"Sie haben ein BMI von {bmi} und sindstark Übergewichtig.")
    elif bmi < 39:
       print(f"Sie haben ein BMI von {bmi} und haben Adipositas Grad II.")
    elif bmi > 40:
      print(f"Sie haben ein BMI von {bmi} und haben Adipositas Grad III.")


gew = int(input("Bitte Geben Sie ihr Körpergewicht an: "))
gr = float(input("Geben Sie hier Ihre Körpergröße an: "))
bmi = gew / ((gr / 100)**2)

if input("Sind Sie M oder W?") == "M":
    bmi_M()
else:
    bmi_W()