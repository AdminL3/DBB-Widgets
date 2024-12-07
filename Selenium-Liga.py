import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.basketball-bund.net/')


time.sleep(1)

# accept cookies
driver.find_element(By.ID, 'cmpbntyestxt').click()

driver.get('https://www.basketball-bund.net/login.do?reqCode=showLogin')

user = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
user.send_keys("211031")
password.send_keys("He1mut@27")
driver.find_element(
    By.CSS_SELECTOR, 'a.button.singleClickAction[href="javascript:login();"][title="klicken Sie hier, um Sich anzumelden!"]').click()

time.sleep(0.2)

driver.get('https://www.basketball-bund.net/index.jsp?Action=8860&sort_liga_altersklasse_sortorder=asc&topsort=liga_altersklasse_sortorder')
tables = driver.find_elements(
    By.CSS_SELECTOR, 'table.sportView[width="100%"][cellpadding="0"][cellspacing="1"][border="0"]')
elements = tables[1].find_elements(By.CSS_SELECTOR, 'tr')

elements.pop(0)
print(f"ELements: {len(elements)}")
abschnitte = []
for element in elements:
    tags = element.find_elements(By.CSS_SELECTOR, "td")
    if len(tags) == 8:
        abschnitte.append(element)

print(len(abschnitte))
Namen = []
Ordnungszahl = []
Spielklasse = []
Altersklasse = []
Geschlecht = []
Liganame = []
Liganummer = []
tags = []
for abschnitt in abschnitte:
    tags = abschnitt.find_elements(By.CSS_SELECTOR, "nobr")
    a_tags = abschnitt.find_elements(By.CSS_SELECTOR, "a")
    if len(tags) >= 2:
        Namen.append(tags[0].text)
        Ordnungszahl.append(tags[1].text)
        Spielklasse.append(tags[2].text)
        Altersklasse.append(tags[3].text)
        Geschlecht.append(tags[4].text)
        Liganame.append(tags[5].text)
        Liganummer.append(tags[6].text.strip())


with open('data/Liga/Namen.txt', 'w', encoding="UTF-8") as file:
    file.writelines(f"{data}\n" for data in Namen)

with open('data/Liga/Ordnungszahl.txt', 'w', encoding="UTF-8") as file:
    file.writelines(f"{data}\n" for data in Ordnungszahl)

with open('data/Liga/Spielklasse.txt', 'w', encoding="UTF-8") as file:
    file.writelines(f"{data}\n" for data in Spielklasse)

with open('data/Liga/Altersklasse.txt', 'w', encoding="UTF-8") as file:
    file.writelines(f"{data}\n" for data in Altersklasse)

with open('data/Liga/Geschlecht.txt', 'w', encoding="UTF-8") as file:
    file.writelines(f"{data}\n" for data in Geschlecht)

with open('data/Liga/Liganame.txt', 'w', encoding="UTF-8") as file:
    file.writelines(f"{data}\n" for data in Liganame)

with open('data/Liga/Liganummer.txt', 'w', encoding="UTF-8") as file:
    file.writelines(f"{data}\n" for data in Liganummer)


for i in range(2):
    time.sleep(1)
driver.quit()
