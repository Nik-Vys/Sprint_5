from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPage, AuthorizationPage
from random import randint


# Генерация логина и email
def random_user_name():
    user_name =f'{randint(0,1000)}@ya.ru'
    return user_name

class TestRegistrationPage:

    # Проверка успешной регистрации пользователя
    def test_registration_completed_registration(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(RegistrationPage.registration_button))
        driver.find_element(*RegistrationPage.name_input).send_keys('Николай')
        driver.find_element(*RegistrationPage.email_input).send_keys(random_user_name())
        driver.find_element(*RegistrationPage.password_input).send_keys(f'{randint(10,99)}asda')
        driver.find_element(*RegistrationPage.registration_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(AuthorizationPage.entrance_name))

        assert 'https://stellarburgers.nomoreparties.site/login' == driver.current_url and driver.find_element(*AuthorizationPage.entrance_name).is_displayed()
        driver.quit()

    # Негативная проверка поля "Пароль" в длину менее 6 символов
    def test_registration_wrong_password_error_appeared(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*RegistrationPage.name_input).send_keys('Никита')
        driver.find_element(*RegistrationPage.email_input).send_keys("nikvys20799@yandex.ru")
        driver.find_element(*RegistrationPage.password_input).send_keys(f'{randint(10,99)}')
        driver.find_element(*RegistrationPage.registration_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrationPage.error_incorrect_password))

        assert 'https://stellarburgers.nomoreparties.site/register' == driver.current_url and 'Некорректный пароль' == driver.find_element(*RegistrationPage.error_incorrect_password).text
        driver.quit()

    # Проверка регистрации с пустым полем "Имя"
    def test_registration_empty_name_registration_failed(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(RegistrationPage.registration_button))
        driver.find_element(*RegistrationPage.email_input).send_keys(random_user_name())
        driver.find_element(*RegistrationPage.password_input).send_keys(f'{randint(10,99)}asda')
        driver.find_element(*RegistrationPage.registration_button).click()

        assert 'https://stellarburgers.nomoreparties.site/register' == driver.current_url and driver.find_element(*RegistrationPage.registration_button).is_displayed()
        driver.quit()
