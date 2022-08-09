# Protekt to claculate how much money everyone has to pay
import copy


class Produkt:
    def __init__(self, name, preis, personen):
        self.name = name
        self.preis = preis
        self.personen = personen


personenNamen = []
zahlenderBetrag = []
personenDabei = []
produkteUebersicht = []
total = 0

print("Welcome to the money programm")

anzahlPersonen = int(input("Geben sie die Anzahl der Personen an: "))

for x in range(anzahlPersonen):
    personenNamen.append(input("Name Person" + str(x + 1) + ": "))

fremdWährung = input("Wird eine Fremdwährung benutzt[y/N]: ")

if fremdWährung == "y":
    fremdWährung = True
elif fremdWährung == "Y":
    fremdWährung = True
else:
    fremdWährung = False

if fremdWährung:
    totalEUR = float (input("Total in EUR: "))
    print("Bitte geben sie die Produktpreis in Fremdwährung an")

print("Geben sie nun alle Produkte an und wenn sie fertig sind schreiben sie bei Produktname fertig")

while True:
    produktAdd = input("Produktname: ")

    if produktAdd == "fertig":
        print("alle produkte wurden eingegeben")
        break

    preis = float(input("Preis: "))

    for x in personenNamen:
        personBool = input("Ist " + str(x) + " dabei [Y/n]: ")
        if personBool == "n":
            personBool = False
        elif personBool == "N":
            personBool = False
        else:
            personBool = True

        if personBool:
            personenDabei.append(x)

    produktAdd = Produkt(produktAdd, copy.deepcopy(preis), copy.deepcopy(personenDabei))

    personenDabei.clear()

    produkteUebersicht.append(produktAdd)

for x in produkteUebersicht:
    total = total + x.preis


for x in personenNamen:
    betrag = 0
    for y in produkteUebersicht:
        if x in y.personen:
            betrag += y.preis / len(y.personen)
    zahlenderBetrag.append(betrag)

if fremdWährung:
    for x in range(len(zahlenderBetrag)):
        zahlenderBetrag[x] = zahlenderBetrag[x] / total * totalEUR

for x in range(len(personenNamen)):
    print(personenNamen[x] + " muss " + str(zahlenderBetrag[x]) + "€ zahlen")