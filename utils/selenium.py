from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

def wait_render(driver, element, type = By.CSS_SELECTOR) -> WebElement:
    return WebDriverWait(driver, timeout=600).until(
        lambda d: d.find_element(type, element)
    )