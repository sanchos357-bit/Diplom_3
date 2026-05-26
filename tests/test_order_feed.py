import time
from selenium.webdriver.common.by import By
import allure
import pytest
from data.Urls import Urls
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.order_feed_page import OrderFeedPage
from pages.auth_user_page import AuthUserPage
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrdersPageLocators
from selenium.webdriver.support import expected_conditions as EC



class TestOrderFeed:


    @allure.title('При создании заказа, происходит увеличения значения счетчиков заказов "Выполнено за все время"/"Выполнено за сегодня"')
    @allure.description('Сверяем счетчик заказов "Выполнено за все время" / "Выполнено за сегодня" до создания заказа и после создания заказа '
                        'Счетчик должен увеличиться')
    @pytest.mark.parametrize('counter', [OrdersPageLocators.TOTAL_ORDER_COUNT, OrdersPageLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, driver, counter):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        auth_user_page = AuthUserPage(driver)
        base_page.go_to_site()
        auth_user_page.login()
        main_page.click_order_list_button()
        prev_counter_value = order_feed_page.get_total_order_count_daily(counter)
        main_page.click_constructor_button()
        main_page.add_filling_to_order()
        main_page.click_order_button()
        main_page.click_close_modal_order()
        main_page.click_order_list_button()
        current_counter_value = order_feed_page.get_total_order_count_daily(counter)
        assert current_counter_value > prev_counter_value, "Заказ не создался, counter не сработал"


    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    @allure.description('Проверяем,что после оформления заказа его номер появляется в разделе «В работе»')
    def test_create_number_order(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        auth_user_page = AuthUserPage(driver)
        base_page.go_to_site()
        auth_user_page.login()
        main_page.add_filling_to_order()
        main_page.click_order_button()
        order_number = main_page.get_with_order_id()
        main_page.click_close_modal_order()
        main_page.click_order_list_button()
        order_number_refactor = main_page.get_user_order(order_number)
        order_in_progress = main_page.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress
