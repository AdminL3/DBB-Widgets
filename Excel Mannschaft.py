import csv

with open('data/Mannschaft/Namen.txt', 'r', encoding='latin-1') as file:
    namen = file.read().splitlines()

with open('data/Mannschaft/Ordnungszahl.txt', 'r', encoding='latin-1') as file:
    ordnungszahl = file.read().splitlines()

with open('data/Mannschaft/Altersklasse.txt', 'r', encoding='latin-1') as file:
    altersklasse = file.read().splitlines()

with open('data/Mannschaft/Geschlecht.txt', 'r', encoding='latin-1') as file:
    geschlecht = file.read().splitlines()

with open('data/Mannschaft/Mannschaft_ID.txt', 'r', encoding='latin-1') as file:
    mannschafts_ID = file.read().splitlines()

with open('data/Mannschaft/Widget_ID.txt', 'r', encoding='latin-1') as file:
    widget_ID = file.read().splitlines()


# Read the content of the code_snippets.txt file
with open('data/Mannschaft/code_snippets_big.txt', 'r', encoding='utf-8') as file:
    code_snippets_big = file.read()
with open('data/Mannschaft/code_snippets_small.txt', 'r', encoding='utf-8') as file:
    code_snippets_small = file.read()

code_snippets_big2 = [snippet.replace('\n', ' ')
                      for snippet in code_snippets_big.strip().split('\n\n')]
code_snippets_small2 = [snippet.replace('\n', ' ')
                        for snippet in code_snippets_small.strip().split('\n\n')]


# export
rows = zip(namen, ordnungszahl, altersklasse,
           geschlecht, mannschafts_ID, widget_ID, code_snippets_big2, code_snippets_small2)

# Write to a CSV file using a semicolon delimiter
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)

    # Write the header
    writer.writerow(['Name', 'Ordnungszahl', 'Altersklasse',
                    'Geschlecht', 'Mannschafts ID', 'Widget ID', 'Code groß', 'Code klein'])

    # Write the data rows
    writer.writerows(rows)
    writer.writerow("")
    writer.writerow(["ä", "ü", "Ü", "ß"])
    writer.writerow(["a", "u", "U", "S"])

print("Created output.csv")
