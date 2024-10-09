import csv

with open('data/Liga/Namen.txt', 'r', encoding='latin-1') as file:
    namen = file.read().splitlines()

with open('data/Liga/Ordnungszahl.txt', 'r', encoding='latin-1') as file:
    ordnungszahl = file.read().splitlines()

with open('data/Liga/Spielklasse.txt', 'r', encoding='latin-1') as file:
    spielklasse = file.read().splitlines()

with open('data/Liga/Altersklasse.txt', 'r', encoding='latin-1') as file:
    altersklasse = file.read().splitlines()

with open('data/Liga/Geschlecht.txt', 'r', encoding='latin-1') as file:
    geschlecht = file.read().splitlines()

with open('data/Liga/Liganame.txt', 'r', encoding='latin-1') as file:
    liganame = file.read().splitlines()

with open('data/Liga/Liganummer.txt', 'r', encoding='latin-1') as file:
    liganummer = file.read().splitlines()

with open('data/Liga/Widget_ID.txt', 'r', encoding='latin-1') as file:
    widget_ID = file.read().splitlines()


# Read the content of the code_snippets.txt file
with open('data/Liga/code_snippets_big.txt', 'r', encoding='utf-8') as file:
    code_snippets_big = file.read()
with open('data/Liga/code_snippets_small.txt', 'r', encoding='utf-8') as file:
    code_snippets_small = file.read()


code_snippets_big2 = [snippet.replace('\n', ' ')
                      for snippet in code_snippets_big.strip().split('\n\n')]
code_snippets_small2 = [snippet.replace('\n', ' ')
                        for snippet in code_snippets_small.strip().split('\n\n')]


# export
rows = zip(namen, ordnungszahl, spielklasse, altersklasse,
           geschlecht, liganame, liganummer, widget_ID, code_snippets_big2, code_snippets_small2)

# Write to a CSV file using a semicolon delimiter
with open('Liga.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)

    # Write the header
    writer.writerow(['Name', 'Ordnungszahl', 'Spielklasse', 'Altersklasse',
                    'Geschlecht', 'Liganame', 'Liganummer', 'Widget ID', 'Code groß', 'Code klein'])

    # Write the data rows
    writer.writerows(rows)
    writer.writerow("")
    writer.writerow(["ä", "ü", "Ü", "ß"])
    writer.writerow(["a", "u", "U", "S"])

print("Created Liga.csv")
