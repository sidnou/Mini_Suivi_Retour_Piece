from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# page_url = 127.0.0.1:8000
class PageTest(object):
    def __init__(self, driver):
        self.driver = driver

    def test_vue_suivi_tnt(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/suivi-tnt/add/')
        titre = browser.title
        assert titre == "Ajout Suivi TNT"
        browser.quit()

    def test_add_suivi_tnt(self):
        # browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/suivi-tnt/add/')

        browser.find_element(By.NAME, "reference").send_keys(f"L99999-999{Keys.TAB}")
        browser.find_element(By.NAME, "numero_commande").send_keys(f"OR99999{Keys.TAB}")
        browser.find_element(By.NAME, "numero_dossier").send_keys(f"M67S-9999-99999{Keys.TAB}")
        browser.find_element(By.NAME, "numero_suivi").send_keys(f"9999999999999999999999{Keys.TAB}")
        # browser.find_element(By.,)
