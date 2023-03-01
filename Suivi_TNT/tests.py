from django.test import TestCase
from Suivi_TNT.models import SuiviRetourPieceHP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


# Create your tests here.

class SuiviRetourPieceHPTestCase(TestCase):
    def setUp(self):
        SuiviRetourPieceHP.objects.create(
            reference="L25426-010",
            numero_commande='OR0425869',
            numero_dossier='M67S-9999-99999',
            numero_suivi='12345678909876'
        )

    def test_SuiviRetourPieceHP(self):
        suivi_tnt = SuiviRetourPieceHP.objects.get(reference="L25426-010",
                                                   numero_commande='OR0425869',
                                                   numero_dossier='M67S-9999-99999',
                                                   numero_suivi='12345678909876')
        self.assertEqual(suivi_tnt.reference, "L25426-010")
        self.assertEqual(suivi_tnt.numero_commande, 'OR0425869')
        self.assertEqual(suivi_tnt.numero_dossier, 'M67S-9999-99999')
        self.assertEqual(suivi_tnt.numero_suivi, '12345678909876')

    def test_vue_suivi_tnt(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/suivi-tnt/add/')
        titre = browser.title
        assert titre == "Ajout Suivi TNT"
        browser.quit()

    def test_add_suivi_tnt(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/suivi-tnt/add/')

        browser.find_element(By.NAME, "reference").send_keys(f"L99999-999{Keys.TAB}")
        browser.find_element(By.NAME, "numero_commande").send_keys(f"OR99999{Keys.TAB}")
        browser.find_element(By.NAME, "numero_dossier").send_keys(f"M67S-9999-99999{Keys.TAB}")
        browser.find_element(By.NAME, "numero_suivi").send_keys(f"9999999999999999999999{Keys.TAB}")
        # browser.find_element(By.,)
