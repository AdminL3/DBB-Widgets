### 1. Get the data using Selenium

- Selenium Liga & Mannschaft

### 2. Get the Widget IDs from urls

- Widget ID Liga and Mannschaft .py

### 3. Generate Code

- Using the data we generate the code snippets for the widgets

### 4. Save as Excel

- Use the Excel Liga and Manschaft .py to export it to a Excel file

### 5. Use the Excel file to generate the widgets

#### 1. Both (Spiele & Tabelle) Widgets

- Example U18
- Run `WP Tabs both.py`
- Enter 2 for 1 und 2 Tab
- Enter Manschaftsindex: See Excel file and count
- Enter For both teams: Here 4 & 5
- Enter Ligaindex: Here: 8 & 7
- Enter Tabname: Here: U18/1 & U18/2
- Paste on wordpress after: Spielplan & Tabelle

#### 2. Using Input file

- See `WP Tabs both input.py`
- Use Input file to specify data

1. Amount
2. Manschaftsindex `* amount`
3. Namen `* amount`

```
2
4
5
Tab 1 Name
Tab 2 Name
```

### Extra

What I did is you can put two widgets together, but that doesnt work for mobile which is why i deleted it.
