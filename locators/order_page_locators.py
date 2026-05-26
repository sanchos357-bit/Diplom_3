from selenium import webdriver
from selenium.webdriver.common.by import By


class OrdersPageLocators:
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem "
                                         "OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")

