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
