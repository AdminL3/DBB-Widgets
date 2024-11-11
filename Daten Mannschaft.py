import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import config

username = config.username
password = config.password

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
user.send_keys(username)
password.send_keys(password)
driver.find_element(
    By.CSS_SELECTOR, 'a.button.singleClickAction[href="javascript:login();"][title="klicken Sie hier, um Sich anzumelden!"]').click()

time.sleep(0.2)

driver.get('https://www.basketball-bund.net/index.jsp?Action=8100')
tables = driver.find_elements(
    By.XPATH, "//table[@class='sportView' and @width='100%' and @cellpadding='0' and @cellspacing='1' and @border='0']")
elements = tables[2].find_elements(By.CSS_SELECTOR, 'tr')


print(f"ELements: {len(elements)}")
abschnitte = []
for element in elements:
    tags = element.find_elements(By.CSS_SELECTOR, "td")
    if len(tags) == 6:
        abschnitte.append(element)

print(len(abschnitte))
Namen = []
Ordnungszahl = []
Altersklasse = []
Geschlecht = []
urls = []
tags = []
for abschnitt in abschnitte:
    tags = abschnitt.find_elements(By.CSS_SELECTOR, "nobr")
    a_tags = abschnitt.find_elements(By.CSS_SELECTOR, "a")
    if len(tags) >= 2:
        Namen.append(tags[0].text)
        Ordnungszahl.append(tags[1].text)
        Altersklasse.append(tags[2].text)
        Geschlecht.append(tags[3].text)
        urls.append(a_tags[-1].get_attribute('href'))


pattern = r'/(\d+)$'
with open('data/Mannschaft/Mannschaft_ID.txt', 'w') as file:
    for data in urls:
        match = re.search(pattern, data)
        if match:
            file.write(f"{match.group(1)}\n")


with open('data/Mannschaft/Namen.txt', 'w') as file:
    file.writelines(f"{data}\n" for data in Namen)

with open('data/Mannschaft/Ordnungszahl.txt', 'w') as file:
    file.writelines(f"{data}\n" for data in Ordnungszahl)

with open('data/Mannschaft/Altersklasse.txt', 'w') as file:
    file.writelines(f"{data}\n" for data in Altersklasse)

with open('data/Mannschaft/Geschlecht.txt', 'w') as file:
    file.writelines(f"{data}\n" for data in Geschlecht)

with open('data/Mannschaft/urls.txt', 'w') as file:
    file.writelines(f"{data}\n" for data in urls)


for i in range(2):
    time.sleep(1)
driver.quit()
