from selenium.webdriver.common.by import By


class TestBurgers:
    def test_sauces(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()  # в раздел "Соусы"
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]/p').text == \
               'Соус Spicy-X'  # наименование соуса

    def test_fillings(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()  # в раздел "Начинки"
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]/p').text == \
            'Говяжий метеорит (отбивная)'  # наименование начинки

    def test_buns(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()  # сперва в раздел "соусы"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click()  # затем в раздел "булки"
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]/p').text == \
               'Краторная булка N-200i'   # наименование булки

