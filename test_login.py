import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

email = "tester@mailinator.com"
name = "Jan"
surname = "Kowalski"
password = "Tester1234@"
birthdate_dmr = ['1', '7', '1987']


# Tworzę nową klasę dziedziczącą
# po TestCase z modułu unittest
# W której zawarte są mechanizmy
# uruchamiania testów
class TestRegistration(unittest.TestCase):
    """
    Mój scenariusz/przypadek testowy
    """

    def setUp(self) -> None:
        """
        Warunki wstępne testu
        """
        # Otwieram przeglądarkę
        self.driver = webdriver.Chrome()
        # ... na stronie http://automationpractice.com/index.php
        self.driver.get("http://automationpractice.com/index.php")
        # Maksymalizuj okno
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # Tutaj będzie prawdziwy test
    def testLogin(self):
        # 1. Kliknij przycisk „Sign in”
        signin_btn = self.driver.find_element_by_class_name("login")
        signin_btn.click()
        # self.driver.find_element_by_class_name("login").click()
        # 2. Wpisz adres e-mail i hasło
        email_input = self.driver.find_element_by_id("email")
        email_input.send_keys(email)
        passwd_input = self.driver.find_element_by_id("passwd")
        passwd_input.send_keys(password)
        # 3. Kliknij „Sign in”
        create_btn = self.driver.find_element_by_name("SubmitLogin")
        create_btn.click()

    def tearDown(self) -> None:
        """
        Porządki po teście
        """
        # Wyłączam przeglądarkę
        self.driver.quit()


# Jeśli nazywam się __main__
if __name__ == "__main__":
    # ...to uruchamiam testy
    unittest.main(verbosity=2)