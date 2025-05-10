from selenium.webdriver.common.by import By


# Страница регистрации
class RegistrationPage:

    name_input = (By.XPATH, "(.//input[@name = 'name'])[1]")        # Поле ввода имени
    email_input = (By.XPATH, "(.//input[@name = 'name'])[2]")       # Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")     # Поле ввода пароля
    registration_button = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")       # Кнопка зарегистрироваться
    login_account_button = (By.XPATH, ".//a[text() = 'Войти']")            # Кнопка войти
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']")        # Кнопка конструктор
    order_feed_button = (By.XPATH, ".//p[text() = 'Лента Заказов']")       # Кнопка лента заказов
    main_logo_button = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")   # Кнопка личного кабинета
    error_incorrect_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']")   # Пароль неверный

# Страница авторизации
class AuthorizationPage:
    
    authorization_form = (By.XPATH, './/div[@class = Auth_login__3hAey]')  # Форма авторизации
    entrance_name = (By.XPATH, ".//h2[text()='Вход']")       # Заголовок "Вход"
    email_input = (By.XPATH, ".//input[@name = 'name']")          # Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")         # Поле ввода пароля
    login_account_button = (By.XPATH, ".//button[text() = 'Войти']")        #Кнопка войти
    registration_button = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")         #Кнопка зарегистрироваться
    recover_password_button = (By.XPATH, ".//a[text() = 'Восстановить пароль']")         #Кнопка восстановить пароль
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']")        #Кнопка конструктор
    order_feed_button = (By.XPATH, ".//p[text() = 'Лента Заказов']")       #Кнопка лента заказов
    main_logo_button = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")       #Кнопка главной страницы сайта
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")        #Кнопка личного кабинета

# Главная страница
class MainPage:

    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")         #Кнопка личного кабинета
    login_account_button = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")      #Кнопка войти
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка оформить заказ
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']")         #Кнопка конструктор
    order_feed_button = (By.XPATH, ".//p[text() = 'Лента Заказов']")        #Кнопка лента заказов
    bun_button = (By.XPATH, ".//span[text() = 'Булки']")        #Кнопка переключения на булки
    bun_name = (By.XPATH, "//h2[text()='Булки']")  # Выбор булок на главной странице
    sauces_button = (By.XPATH, ".//span[text() = 'Соусы']")         #Кнопка переключения на соусы
    sauces_name = (By.XPATH, "//h2[text()='Соусы']")    # Выбор соусов на главной странице
    toppings_button = (By.XPATH, ".//span[text() = 'Начинки']")         #Кнопка переключения на начинки
    toppings_name = (By.XPATH, "//h2[text()='Начинки']")  # Выбор начинок на главной странице

# Страница личного кабинета
class PersonalAccountPage:

    personal_account_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")     #Форма личного кабинета
    profile_button = (By.XPATH, ".//a[text() = 'Профиль']")     #Кнопка профиль
    order_history_button = (By.XPATH, ".//a[text() = 'История заказов']")   #Кнопка история заказов
    logout_button = (By.XPATH, ".//button[text() = 'Выход']")   #Кнопка выход
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")     #Кнопка сохранить
    cancel_button = (By.XPATH, ".//button[text() = 'Отмена']")      #Кнопка отмена
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']")     #Кнопка конструктор
    order_feed_button = (By.XPATH, ".//p[text() = 'Лента Заказов']")    #Кнопка лента заказов
    main_logo_button = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")   #Кнопка главной страницы сайта
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")     #Кнопка личного кабинета

class RecoverPasswordPage:

    email_input = (By.XPATH, ".//label[text() = 'Email']")      #Поле ввода email
    recover_button = (By.XPATH, ".//button[text() = 'Восстановить']")      #Кнопка восстановить
    login_account_button = (By.XPATH, ".//a[text() = 'Войти']")        #Кнопка войти
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']")        # Кнопка конструктор
    order_feed_button = (By.XPATH, ".//p[text() = 'Лента Заказов']")       # Кнопка лента заказов
    main_logo_button = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    personal_account_button = (By.XPATH, ".//p[text() = 'Личный Кабинет']")   # Кнопка личного кабинета