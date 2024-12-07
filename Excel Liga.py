from openpyxl import Workbook

# Create a new workbook and select the active worksheet
workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Liga Data"

# Read data from files
with open('data/Liga/Namen.txt', 'r', encoding='UTF-8') as file:
    namen = file.read().splitlines()

with open('data/Liga/Ordnungszahl.txt', 'r', encoding='UTF-8') as file:
    ordnungszahl = file.read().splitlines()

with open('data/Liga/Spielklasse.txt', 'r', encoding='UTF-8') as file:
    spielklasse = file.read().splitlines()

with open('data/Liga/Altersklasse.txt', 'r', encoding='UTF-8') as file:
    altersklasse = file.read().splitlines()

with open('data/Liga/Geschlecht.txt', 'r', encoding='UTF-8') as file:
    geschlecht = file.read().splitlines()

with open('data/Liga/Liganame.txt', 'r', encoding='UTF-8') as file:
    liganame = file.read().splitlines()

with open('data/Liga/Liganummer.txt', 'r', encoding='UTF-8') as file:
    liganummer = file.read().splitlines()

with open('data/Liga/Widget_ID.txt', 'r', encoding='UTF-8') as file:
    widget_ID = file.read().splitlines()

# Read the content of the code_snippets.txt files
with open('data/Liga/code_snippets_big.txt', 'r', encoding='utf-8') as file:
    code_snippets_big = file.read()
with open('data/Liga/code_snippets_small.txt', 'r', encoding='utf-8') as file:
    code_snippets_small = file.read()

# Process the snippets
code_snippets_big2 = [snippet.replace('\n', ' ')
                      for snippet in code_snippets_big.strip().split('\n\n')]
code_snippets_small2 = [snippet.replace('\n', ' ')
                        for snippet in code_snippets_small.strip().split('\n\n')]

# Combine rows
rows = zip(namen, ordnungszahl, spielklasse, altersklasse,
           geschlecht, liganame, liganummer, widget_ID, code_snippets_big2, code_snippets_small2)

# Write the header to the worksheet
worksheet.append(['Name', 'Ordnungszahl', 'Spielklasse', 'Altersklasse',
                  'Geschlecht', 'Liganame', 'Liganummer', 'Widget ID', 'Code groß', 'Code klein'])

# Write the data rows to the worksheet
for row in rows:
    worksheet.append(row)

# Save the workbook to an Excel file
workbook.save('data/Liga.xlsx')

print("Created Liga.xlsx")
