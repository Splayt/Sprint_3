from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurgers:
    def test_move_constructor(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()  # кнопка Личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys\
            ('splayt0908@yandex.ru')  # поле Email

        # поле Пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()  # кнопка Войти
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()  # переход в Личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p').click()   # кнопка Конструктор

        move = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main\
        /section[1]/div[2]/ul[1]/a[1]/p'))).text   # ожидание появления названия булки
        assert move == 'Флюоресцентная булка R2-D3'

    def test_move_logo(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()  # кнопка Личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys \
            ('splayt0908@yandex.ru')  # поле Email

        # поле Пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()  # кнопка Войти
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()  # переход в Личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div').click()  # переход на логотип

        move = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main\
               /section[1]/div[2]/ul[1]/a[1]/p'))).text  # ожидание появления названия булки
        assert move == 'Флюоресцентная булка R2-D3'