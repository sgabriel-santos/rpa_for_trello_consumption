from utils import selenium as sl
import config.credentials as credentials
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

def do_login(driver: WebElement):
    driver.find_element(By.XPATH, '//*[@id="BXP-APP"]/header[1]/div/div[1]/div[2]/a[1]').click()
    ipt_email = sl.wait_render(driver, '//*[@id="user"]', By.XPATH)
    ipt_email.send_keys(credentials.LOGIN)

    btn_continue = driver.find_element(By.XPATH, '//*[@id="login"]').click()
    btn_continue = sl.wait_render(driver, 'login-submit', By.ID)
    
    ipt_password = sl.wait_render(driver, '//*[@id="password"]', By.XPATH)
    ipt_password.send_keys(credentials.PASSWORD)

    btn_continue.click()

def open_board(driver: WebElement, board: str):
    board: WebElement = sl.wait_render(driver, f'[title={board}]', By.CSS_SELECTOR)
    board.click()

def do_export(driver: WebElement):
    btn_more = sl.wait_render(driver, 'js-open-more', By.CLASS_NAME)
    
    try:
        btn_option = sl.wait_render(driver, '.show-sidebar-button-react-root button', By.CSS_SELECTOR)
        btn_option.click()
    except:
        pass
    
    btn_more.click()

    btn_share = sl.wait_render(driver, 'js-share', By.CLASS_NAME)
    btn_share.click()

    btn_export_json = sl.wait_render(driver, 'js-export-json', By.CLASS_NAME)
    btn_export_json.click()

    json_data = sl.wait_render(driver, 'body > pre', By.CSS_SELECTOR)

    with open('trello.json', 'w', encoding='utf-8') as file:
        file.write(json_data.text)