from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPage
from confitest import driver

class TestConstructorPage:

    # Переход к разделу "Булки"
    def test_move_to_bun_move_done(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.bun_button))
        driver.execute_script("arguments[0].click();", driver.find_element(*MainPage.bun_button))
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.bun_name))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(*MainPage.bun_name).is_displayed()

    # Переход к разделу "Соусы"
    def test_move_to_sauces_move_done(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.sauces_button))
        driver.execute_script("arguments[0].click();", driver.find_element(*MainPage.sauces_button))
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.sauces_name))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(*MainPage.sauces_name).is_displayed()

    # Переход к разделу "Начинки"
    def test_move_to_toppings_move_done(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.toppings_button))
        driver.execute_script("arguments[0].click();", driver.find_element(*MainPage.toppings_button))
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(MainPage.toppings_name))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(*MainPage.toppings_name).is_displayed()