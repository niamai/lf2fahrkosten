# user gets a greeting.
print("Hallo!")


def check_is_digit(input_str):
    if not input_str.isdigit():
        check_is_digit(input("Geben Sie bitte eine glatte Zahl ein: "))
    else:
        global correct_input
        correct_input = input_str


# user should choose how many meters the ride was.
distanz_input = input(
    "Bitte tragen Sie ein, wie viele Meter Sie gefahren sind? ")
check_is_digit(distanz_input)
distanz = correct_input

# user should input the duration of the ride.
zeit_input = input(
    "Bitte tragen Sie ein, wie viele Minuten Sie gefahren sind? ")
check_is_digit(zeit_input)
zeit = correct_input

# berechnung des Preises in eurocent.
if zeit.isdigit() and distanz.isdigit():
    preis_cent = (float(distanz) * 0.2 + int(zeit) * 10) / 100
    preis_cent = str(round(preis_cent, 2))
    #vor_komma = preis_cent[:len(preis_cent)-2]
    #nach_komma = preis_cent[len(preis_cent)-2:]

    preis_euro = preis_cent.replace(".", ",")

#  Überprüfung, ob es nur eine Minute ist
if zeit == "1":
    minute = "Minute"
else:
    minute = "Minuten"

# preis wird zurueckgegeben
print("Sie sind", distanz, "Meter und", zeit, minute,
      "gefahren. Somit ergibt ein Preis von:",  preis_euro + "€.")
