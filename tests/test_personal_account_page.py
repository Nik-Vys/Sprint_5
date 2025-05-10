from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import  MainPage, PersonalAccountPage, AuthorizationPage
from confitest import login_driver

class TestPersonalAccount:

    # Проверка перехода по клику на «Личный кабинет»
    def test_move_personal_account_from_main_page_move_done(self, login_driver):
        driver = login_driver
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.personal_account_button))
        driver.find_element(*MainPage.personal_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PersonalAccountPage.personal_account_form))

        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url and driver.find_element(*PersonalAccountPage.logout_button).text == 'Выход'
        driver.quit()

    # Проверка перехода по клику на «Конструктор»
    def test_move_main_page_from_personal_account_by_clicking_constructor_button_move_done(self, login_driver):
        driver = login_driver
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.personal_account_button))
        driver.find_element(*MainPage.personal_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PersonalAccountPage.personal_account_form))
        driver.find_element(*PersonalAccountPage.constructor_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.place_order_button))

        assert driver.find_element(*MainPage.place_order_button).text == "Оформить заказ" and driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    # Проверка перехода по клику на логотип Stellar Burgers
    def test_move_main_page_from_personal_account_by_clicking_main_logo_button_move_done(self, login_driver):
        driver = login_driver
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.personal_account_button))
        driver.find_element(*MainPage.personal_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PersonalAccountPage.personal_account_form))
        driver.find_element(*PersonalAccountPage.main_logo_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.place_order_button))

        assert driver.find_element(*MainPage.place_order_button).text == "Оформить заказ" and driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()


    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_logout_personal_account_logout_done(self, login_driver):
        driver = login_driver
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.personal_account_button))
        driver.find_element(*MainPage.personal_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PersonalAccountPage.personal_account_form))
        driver.find_element(*PersonalAccountPage.logout_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.entrance_name))

        assert driver.find_element(*AuthorizationPage.login_account_button).text == "Войти" and driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
