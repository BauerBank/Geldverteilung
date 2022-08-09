# Protekt to claculate how much money everyone has to pay

import copy


class Produkt:
    # Product class to safe the parameters for every product
    def __init__(self, name, preis, personen):
        self.name = name
        self.preis = preis
        self.personen = personen


# init every list as an empty list
personenNamen = []
zahlenderBetrag = []
personenDabei = []
produkteUebersicht = []
totalEUR = 0
# init total as zero
total = 0

# print welcome message
print("Moin")

# input and safe the number of persons
anzahlPersonen = int(input("Geben sie die Anzahl der Personen an: "))

# safe the name for every person
for x in range(anzahlPersonen):
    personenNamen.append(input("Name Person" + str(x + 1) + ": "))

# ask if another currency than EUR is used
fremdWaehrung = input("Wird eine Fremdwährung benutzt[y/N]: ")

# convert the answer in a bool statement
if fremdWaehrung == "y":
    fremdWaehrung = True
elif fremdWaehrung == "Y":
    fremdWaehrung = True
else:
    fremdWaehrung = False

# if it is another currency ask the total in EUR
if fremdWaehrung:
    totalEUR = float(input("Total in EUR: "))
    print("Bitte geben sie die Produktpreis in Fremdwährung an")

# instructions on how to use the following section
print("Geben sie nun alle Produkte an und wenn sie fertig sind schreiben sie bei Produktname fertig")

# endless loop
while True:

    # ask of a new product name
    produktAdd = input("Produktname: ")

    # if the product is "fertig" leaf the endless loop
    if produktAdd == "fertig":
        print("alle produkte wurden eingegeben")
        break

    # ask the price of the product
    preisoftheproduct = float(input("Preis: "))

    # ask for every person if he/she pays for the product
    for x in personenNamen:
        personBool = input("Ist " + str(x) + " dabei [Y/n]: ")
        if personBool == "n":
            personBool = False
        elif personBool == "N":
            personBool = False
        else:
            personBool = True

        # if a person pays for a product add him to the list
        if personBool:
            personenDabei.append(x)

    # init the product object with deep copy
    produktAdd = Produkt(produktAdd, copy.deepcopy(preisoftheproduct), copy.deepcopy(personenDabei))

    # clear the list for the next object
    personenDabei.clear()

    # add the object to the list of all product objects
    produkteUebersicht.append(produktAdd)

# calculate the total for every person in the used currency
for x in personenNamen:
    betrag = 0
    for y in produkteUebersicht:
        if x in y.personen:
            betrag += y.preis / len(y.personen)
    zahlenderBetrag.append(betrag)

# when another currency is used calculate the total und convert it in EUR
if fremdWaehrung:

    # total
    for x in produkteUebersicht:
        total = total + x.preis

    # convert in EUR
    for x in range(len(zahlenderBetrag)):
        zahlenderBetrag[x] = zahlenderBetrag[x] / total * totalEUR

# print the total for every person
for x in range(len(personenNamen)):
    print(personenNamen[x] + " muss " + str(zahlenderBetrag[x]) + "€ zahlen")
