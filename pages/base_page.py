import allure
from data.Urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент на странице')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url    

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.url_main_page
        self.driver.get(url)    

    @allure.step('Подождать пока элемент станет виден')
    def wait_before_assert(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать пока элемент станет невидим')
    def wait_before_invisibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))   

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))    
    
    @allure.step('Проверить присутствие элемента на странице')
    def check_presense(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step('Дождаться кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Кликаем по элементу {locator}')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Вставить текст {text}')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Переместиться до элемента и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform() 

    @allure.step('Дождаться появления текста в элементе')
    def wait_for_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(locator, text)) 

    @allure.step('Дождаться смены числа в счетчике')
    def wait_before_count_value_changed(self, prev_counter_value, main_page):
        WebDriverWait(self.driver, 20).until(lambda _: int(main_page.get_count_value()) > prev_counter_value)       





        

        

        





