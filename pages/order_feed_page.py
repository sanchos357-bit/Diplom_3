import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from locators.base_page_locators import BasePageLocator
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrdersPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class OrderFeedPage(MainPage):

    @allure.step("Получение количества заказов")
    def get_total_order_count_daily(self, locator):
        return self.get_actually_text(locator)
    
    
    



