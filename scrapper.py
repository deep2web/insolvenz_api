from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from bs4 import BeautifulSoup

from time import sleep

# Get data vis selenium

driver = webdriver.Chrome()


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




# Anzahl der Zeilen in der Tabelle
num_rows = 48  # Setzen Sie dies auf die tatsächliche Anzahl der Zeilen

for i in range(num_rows):
    # Generieren Sie die ID dynamisch
    id_datum = f"tbl_ergebnis:{i}:otx_datum"
    id_aktenzeichen = f"tbl_ergebnis:{i}:otx_azAkt"
    id_schuldner = f"tbl_ergebnis:{i}:otx_schuldner"
    id_sitz = f"tbl_ergebnis:{i}:otx_Sitz"

    # Extrahieren Sie die Daten
    datum = soup.find('span', {'id': id_datum}).text
    aktenzeichen = soup.find('span', {'id': id_aktenzeichen}).text
    schuldner_name = soup.find('span', {'id': id_schuldner}).text
    sitz = soup.find('span', {'id': id_sitz}).text

    # Drucken Sie die extrahierten Daten
    print(f"Veröffentlichungsdatum: {datum}")
    print(f"Aktenzeichen: {aktenzeichen}")
    print(f"Schuldner Name: {schuldner_name}")
    print(f"Wohnsitz: {sitz}")
    print("---")
sleep(5)
driver.close()
