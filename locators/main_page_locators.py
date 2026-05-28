from selenium import webdriver
from selenium.webdriver.common.by import By



class MainPageLocators:
    ORDERS_LIST_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    INGREDIENT_DETAILS_WINDOW = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')
    ORDER_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")
    LOGIN_PROFILE_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    PROFILE_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    LOADING_MODAL = (By.CLASS_NAME, "Modal_modal__loading__3534A")
    MODAL_OVERLAY = (By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")
    