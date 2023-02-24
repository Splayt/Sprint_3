from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()


class TestBurgers:
    def test_registration(self, driver):
        email = faker.email()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()  # Кнопка "Личный кабинет"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()  # Кнопка "Зарегистрироваться"

        # поле Имя
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Egor')

        # Поле "Email"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)

        # Поле "Пароль"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()  # Кнопка "Зарегистрироваться"

        reg = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(),\
        "Войти")]'))).text  # Переход на страницу авторизации
        assert reg == 'Войти'

    def test_incorrect_password(self, driver):   #
        email = faker.email()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()   # Кнопка "Личный кабинет"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()   # Кнопка "Зарегистрироваться"

        # Поле "Имя"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Egor')

        # Поле "Email"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(email)

        # Поле "Пароль"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123')

        # Кнопка "Зарегистрироваться"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == \
               'Некорректный пароль'   # Появившееся уведомление

