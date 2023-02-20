from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurgers:
    def test_authorization_homepage(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()  # кнопка Личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys\
            ('splayt0908@yandex.ru')  # поле Email

        # поле Пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()  # кнопка Войти

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section\
        [2]/div/button')))  # кнопка Оформить заказ

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'

    def test_authorization_personal_page(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()  # кнопка Войти в аккаунт
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys\
            ('splayt0908@yandex.ru')  # поле Email

        # поле Пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()  # кнопка Войти

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section\
        [2]/div/button')))  # кнопка Оформить заказ

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'

    def test_authorization_registration_form(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()  # кнопка Личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()   # кнопка Зарегистрироваться
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()   # Уже зарегистрированы? Войти
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys\
            ('splayt0908@yandex.ru')  # поле email

        # поле Пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()  # кнопка Войти

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section\
        [2]/div/button')))   # кнопка Оформить заказ

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'

    def test_authorization_restore_pass(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()  # кнопка личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()  # кнопка Восстановить пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()  # кнопка Войти
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys\
            ('splayt0908@yandex.ru')  # поле Email

        # поле Пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()  # кнопка Войти

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section\
        [2]/div/button')))  # кнопка Оформить заказ

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'

