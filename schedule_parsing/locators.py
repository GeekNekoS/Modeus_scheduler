from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_INPUT = (By.XPATH, "//input[@placeholder='proverka@example.com']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//span[@class='submit']")


class ModeusLocators:
    MATH_BUTTON = (By.XPATH, "//div[text()=' Математика ']")
    MATH_BASIC_LEVEL_BUTTON = (By.XPATH, "//div[text()=' Математика. Базовый уровень. ']")
    MODULE_SCHEDULE_BUTTON = (By.XPATH, "//a[text()=' Расписание модуля ']")
    #
    MODULES_BUTTONS = (By.XPATH, "//tbody[@class='p-element p-datatable-tbody']/tr/td/div/span")
    ENGLISH_LESSON = (By.XPATH, "//div[text()=' Иностранный язык ']")
    ENGLISH_LEVEL_BUTTON = (By.XPATH, "//div[text()=' Иностранный язык (Смешанное, УрФУ, СМУДС) Часть 1.B2-C1. ИРИТ-РТФ, ИнФО ']")
    #
    ITIS_LESSON_BUTTON = (By.XPATH, "//div[text()=' Информационные технологии и сервисы ']")
    ITIS_1_MODULE = (By.XPATH, "//div[text()=' Информатика для инженеров и исследователей (Онлайн, МИСИС, ОК) ']")
    ITIS_2_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы (онлайн, ИТМО, ОК) ']")
    ITIS_3_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы (онлайн, УрФУ, ОК, ИНЖ) ']")
    ITIS_4_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты инженерного моделирования ']")
    ITIS_5_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты работы с документами ']")
    ITIS_6_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы (Смешанное, УрФУ, ОК). Мастерская Цифровые инструменты твердотельного 3D-моделирования ']")
    ITIS_7_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы. Цифровые инструменты визуализации данных ']")
    ITIS_8_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы. Цифровые инструменты исследовательской деятельности ']")
    ITIS_9_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы. Цифровые инструменты моделирования для 3D-печати ']")
    ITIS_10_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы. Цифровые инструменты обработки данных ']")
    ITIS_11_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы. Цифровые инструменты полигонального 3D-моделирования ']")
    ITIS_12_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы. Цифровые инструменты проектирования игр ']")
    ITIS_13_MODULE = (By.XPATH, "//div[text()=' Информационные технологии и сервисы. Цифровые инструменты проектирования умного дома ']")


class LogoutLocators:
    # LOG_OUT = (By.XPATH, "//img[@class='user-pic__image']")
    # LOG_OUT_BUTTON = (By.XPATH, "//*[text()='Выйти']")
    pass
