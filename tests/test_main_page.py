import allure
from data.Urls import Urls
from pages.main_page import MainPage
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class TestMainPage:
    
    @allure.title('При нажатии на кнопку "Конструктор" происходит переход на страницу сбора бургера')
    @allure.description('Проверка что, на домашней странице при нажатии кнопки "Конструктор" '
                        'происходит корректный переход на страницу сбора бургера.')
    def test_click_constructor_button_go_to_constructor(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.click_order_list_button()
        main_page.click_constructor_button()
        current_url = main_page.current_url()

        assert Urls.url_main_page in current_url


    @allure.title('При нажатии на кнопку "Лента Заказов" происходит переход на страницу заказов')
    @allure.description('Проверка что, на домашней странице при нажатии кнопки "Лента Заказов" '
                        'происходит корректный переход на страницу заказов.')    
    def test_click_order_list_button(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.click_order_list_button()
        current_url = main_page.current_url()

        assert Urls.url_orders_list_page in current_url


    @allure.title('При нажатии на кнопку ингредиент появляется всплывающее окно с деталями')    
    @allure.description('Проверка что, на домашней странице при нажатии на ингредиент '
                        'появляется всплывающее окно с деталями.')
    def test_click_ingredient_appear_detail_window(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.click_ingredient()
        actually_text = main_page.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

        
    @allure.title('При нажатии на крестик окно с деталями ингредиента закрывается') 
    @allure.description('Проверка что, при нажатии на крестик всплывающее окно с'
                        'деталями ингредиента закрывается.')
    def test_click_cross_close_detail_window(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.click_ingredient()
        main_page.click_cross_button()
        main_page.invisibility_ingredient_details()
        assert main_page.check_displayed_ingredient_details() == False


    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается') 
    @allure.description('Проверка что, при добавлении ингредиента в заказ счётчик этого'
                        'ингредиента увеличивается')  
    def test_add_ingredient_counter_increases(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        prev_counter_value = int(main_page.get_count_value())
        main_page.add_filling_to_order()

        wait = WebDriverWait(driver, 20)
        wait.until(lambda _: int(main_page.get_count_value()) > prev_counter_value)

        actual_value = int(main_page.get_count_value())
        assert actual_value > prev_counter_value

