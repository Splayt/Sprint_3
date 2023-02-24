from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBurgers:
    def test_logout(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()  # кнопка Личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys\
            ('splayt0908@yandex.ru')  # поле Email

        # поле Пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()  # кнопка Войти

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]\
        /div/button')))  # кнопка оформить заказ

        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()  # переход в раздел Личный кабинет

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul\
        /li[3]/button')))  # ожидание кнопки выход

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button').click()  # кнопка Выход
        logout = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main\
        /div/form/button'))).text  # ожидание кнопки Войти
        assert logout == 'Войти'