import csv
from openpyxl import Workbook

# Create a new workbook and select the active worksheet
workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Liga Data"

with open('data/Mannschaft/Namen.txt', 'r', encoding='utf8') as file:
    namen = file.read().splitlines()

with open('data/Mannschaft/Ordnungszahl.txt', 'r', encoding='UTF-8') as file:
    ordnungszahl = file.read().splitlines()

with open('data/Mannschaft/Altersklasse.txt', 'r', encoding='UTF-8') as file:
    altersklasse = file.read().splitlines()

with open('data/Mannschaft/Geschlecht.txt', 'r', encoding='UTF-8') as file:
    geschlecht = file.read().splitlines()

with open('data/Mannschaft/Mannschaft_ID.txt', 'r', encoding='UTF-8') as file:
    mannschafts_ID = file.read().splitlines()

with open('data/Mannschaft/Widget_ID.txt', 'r', encoding='UTF-8') as file:
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


# Write the header to the worksheet
worksheet.append(['Name', 'Ordnungszahl', 'Spielklasse', 'Altersklasse',
                  'Geschlecht', 'Liganame', 'Liganummer', 'Widget ID', 'Code groß', 'Code klein'])

# Write the data rows to the worksheet
for row in rows:
    worksheet.append(row)

# Save the workbook to an Excel file
workbook.save('data/Mannschaft.xlsx')

print("Created Mannschaft.xlsx")
