import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser = request.param  

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")

    yield driver  
    driver.quit() 


