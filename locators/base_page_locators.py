from selenium import webdriver
from selenium.webdriver.common.by import By



class BasePageLocator:
    ORDERS_LIST_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'