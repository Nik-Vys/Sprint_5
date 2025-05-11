from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPage, AuthorizationPage, MainPage, RecoverPasswordPage
from confitest import driver


class TestLogin:

    # Проверка входа по кнопке «Войти в аккаунт» на главной
    def test_login_account_button_on_main_page_login_done(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*MainPage.login_account_button).click()
        driver.find_element(*AuthorizationPage.email_input).send_keys("nikvys20799@yandex.ru")
        driver.find_element(*AuthorizationPage.password_input).send_keys("55asda")
        driver.find_element(*AuthorizationPage.login_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.place_order_button))

        assert driver.find_element(*MainPage.place_order_button).text == "Оформить заказ" and driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    # Проверка входа через кнопку «Личный кабинет» на главной
    def test_login_personal_account_button_on_main_page_login_done(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*MainPage.personal_account_button).click()
        driver.find_element(*AuthorizationPage.email_input).send_keys("nikvys20799@yandex.ru")
        driver.find_element(*AuthorizationPage.password_input).send_keys("55asda")
        driver.find_element(*AuthorizationPage.login_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.place_order_button))

        assert driver.find_element(*MainPage.place_order_button).text == "Оформить заказ" and driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверка входа через кнопку в форме регистрации
    def test_login_on_registration_page_login_done(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*RegistrationPage.login_account_button).click()
        driver.find_element(*AuthorizationPage.email_input).send_keys("nikvys20799@yandex.ru")
        driver.find_element(*AuthorizationPage.password_input).send_keys("55asda")
        driver.find_element(*AuthorizationPage.login_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.place_order_button))

        assert driver.find_element(*MainPage.place_order_button).text == "Оформить заказ" and driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверка входа через кнопку в форме восстановления пароля
    def test_login_on_recover_password_page_login_done(self,driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*RecoverPasswordPage.login_account_button).click()
        driver.find_element(*AuthorizationPage.email_input).send_keys("nikvys20799@yandex.ru")
        driver.find_element(*AuthorizationPage.password_input).send_keys("55asda")
        driver.find_element(*AuthorizationPage.login_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.place_order_button))

        assert driver.find_element(*MainPage.place_order_button).text == "Оформить заказ" and driver.current_url == 'https://stellarburgers.nomoreparties.site/'