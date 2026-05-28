import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocator
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrdersPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    
    @allure.step('Нажать на кнопку "Лента Заказов"')
    def click_order_list_button(self):
        self.wait_before_invisibility(MainPageLocators.LOADING_MODAL)
        element = self.find_element(BasePageLocator.ORDERS_LIST_BUTTON)
        return element.click()
    
    @allure.step('Нажать на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.wait_for_element_to_be_clickable(BasePageLocator.CONSTRUCTOR_BUTTON)
        return self.find_element(BasePageLocator.CONSTRUCTOR_BUTTON).click()
    
    @allure.step('Нажать на кнопку ингредиента')
    def click_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.click_on_element(MainPageLocators.BUN_INGREDIENT)
    
    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_show_window_with_details(self):
        self.wait_before_assert(MainPageLocators.INGREDIENT_DETAILS_WINDOW)
        return self.get_actually_text(MainPageLocators.INGREDIENT_DETAILS_WINDOW)
    
    @allure.step('Получить текущий текст')
    def get_actually_text(self, locator):
        self.wait_before_assert(locator)
        actually_text = self.driver.find_element(*locator).text
        return actually_text
    
    @allure.step('Закрываем окно с деталями крестиком')
    def click_cross_button(self):
        self.find_element(MainPageLocators.CROSS_BUTTON).click()

    @allure.step('Проверить скрытость деталей ингредиентов')
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_WINDOW)    

    @allure.step('Проверить наличие деталей ингредиентов на экране')
    def check_displayed_ingredient_details(self) -> bool:
        return self.check_presense(MainPageLocators.INGREDIENT_DETAILS_WINDOW).is_displayed()   

    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_value(self):
        return self.get_actually_text(MainPageLocators.INGREDIENT_COUNTER) 
    
    @allure.step('Добавить ингридиент в заказ')
    def add_filling_to_order(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.wait_before_assert(MainPageLocators.ORDER_BASKET)
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Кликаем по элементу {locator}')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()    

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, locator_one, locator_two):
        self.find_element(locator_one)
        self.find_element(locator_two)

        element_from = self.driver.find_element(*locator_one)
        element_to = self.driver.find_element(*locator_two)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)  

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)  

    @allure.step("Закрыть модальное окно после создания заказа")
    def click_close_modal_order(self):
        locator = MainPageLocators.CLOSE_MODAL_ORDER
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait_before_invisibility(MainPageLocators.MODAL_OVERLAY)

    @allure.step('Получение ORDER_ID')
    def get_with_order_id(self):
        self.wait_before_assert(MainPageLocators.ORDER_IDENTIFICATE)
        order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_actually_text(MainPageLocators.ORDER_ID)
        return f"{order_id}" 

    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        order_refactor = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(OrdersPageLocators.NUMBER_IN_PROGRESS, order_refactor)
        return order_refactor  

    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_actually_text(OrdersPageLocators.NUMBER_IN_PROGRESS)              