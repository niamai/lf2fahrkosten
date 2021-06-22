# der Benutzer erhält eine Begrüßung
print("Herzlichen Dank für die Nutzung der ScooTeq E-Roller!")


def check_is_digit(input_str):
    if not input_str.isdigit():
        check_is_digit(input("Geben Sie bitte eine glatte Zahl ein: "))
    else:
        global correct_input
        correct_input = input_str


# der Benutzer soll die Länge der Fahrt in Metern eingeben
check_is_digit(input(
    "Bitte tragen Sie ein, wie viele Meter Sie gefahren sind: "))
distanz = correct_input

# der Benutzer soll die Dauer der Fahrt in Minuten eingeben
check_is_digit(input(
    "Bitte tragen Sie ein, wie viele Minuten Sie gefahren sind: "))
zeit = correct_input

# Berechnung des Preises in Eurocent.
if zeit.isdigit() and distanz.isdigit():
    preis_cent = (float(distanz) * 0.2 + int(zeit) * 10) / 100
    preis_cent = str("{:.2f}".format(preis_cent))
    preis_euro = preis_cent.replace(".", ",")

#  Überprüfung, ob es nur eine Minute ist
if zeit == "1":
    minute = "Minute"
else:
    minute = "Minuten"

# Preis wird zurueckgegeben
print("Sie sind", distanz, "Meter und", zeit, minute,
      "gefahren. Somit ergibt sich ein Preis von:",  preis_euro + "€.")
