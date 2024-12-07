import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with open('data/Mannschaft/urls.txt', 'r', encoding='utf-8') as file:
    urls = file.read().splitlines()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-search-engine-choice-screen")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
Widget_IDs = []

for url in urls:
    driver.get(url)
    div = driver.find_element(By.CLASS_NAME, "widget-code")
    spans = div.find_elements(By.CSS_SELECTOR, "span")
    text = spans[1].text
    widget_id = re.findall(r'widget_(\d+)', text)
    if widget_id:
        # Append only the first (and likely only) match
        Widget_IDs.append(widget_id[0])

print(Widget_IDs)

with open('data/Mannschaft/Widget_ID.txt', 'w', encoding="UTF-8") as file:
    file.writelines(f"{data}\n" for data in Widget_IDs)


for i in range(4):
    time.sleep(1)
    print(4-i)
driver.quit()
