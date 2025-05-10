from selenium import webdriver
import pytest
from locators import AuthorizationPage, MainPage

@pytest.fixture
def login_driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*MainPage.personal_account_button).click()
    driver.find_element(*AuthorizationPage.email_input).send_keys("nikvys20799@yandex.ru")
    driver.find_element(*AuthorizationPage.password_input).send_keys("55asda")
    driver.find_element(*AuthorizationPage.login_account_button).click()
    return driver