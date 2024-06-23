from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

from time import sleep

# Get data vis selenium
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://neu.insolvenzbekanntmachungen.de/ap/suche.jsf")

title = driver.title
driver.implicitly_wait(2)
print(title)


select_bundesland = driver.find_element(By.XPATH, "//select[@id='frm_suche:lsom_bundesland:lsom']") # XPath des Feldes Bundesland | Bundesland auswählen
select = Select(select_bundesland)
select.select_by_visible_text("Niedersachsen")

sleep(1)

select_gericht = driver.find_element(By.XPATH, "//select[@id='frm_suche:lsom_gericht:lsom']") # XPath des Feldes Gericht  | Gericht auswählen
select = Select(select_gericht)
select.select_by_visible_text("Aurich")

submit_button = driver.find_element(By.XPATH, "//input[@id='frm_suche:cbt_suchen']")    # XPath des Senden Buttons | Formular absenden
submit_button.send_keys("\n")   # Enter Taste drücken, um Formular abzusenden, da Maus Klick nicht funktioniert

# Parse HTML via BeautifulSoup
html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'html.parser')

schuldner_name = soup.find_all('span', class_='withespace')
for title in schuldner_name:
    print(title.text)


sleep(5)
driver.close()
