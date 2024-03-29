from utils import selenium as sl
import config.credentials as credentials
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep

def do_login(driver: WebDriver):
    ipt_email = sl.wait_render(driver, 'user', By.ID)
    ipt_email.send_keys(credentials.LOGIN)

    btn_continue = driver.find_element(By.ID, 'login').click()
    btn_continue = sl.wait_render(driver, 'login-submit', By.ID)
    sleep(1)
    ipt_password = sl.wait_render(driver, 'password', By.ID)
    ipt_password.send_keys(credentials.PASSWORD)

    btn_continue.click()

def do_export(driver: WebDriver, board_name: str):
    sl.wait_render(driver, 'boards-page-board-section-list', By.CLASS_NAME)
    try:
        board = driver.find_element(By.CSS_SELECTOR, f'a.board-tile:has([title="{board_name}"])')
    except:
        print(f'Board {board_name} not found')
        return False
    
    href = board.get_attribute('href')
    url_json = href[:href.rfind('/')] + '.json'
    driver.get(url_json)
    json_data = sl.wait_render(driver, 'body > pre', By.CSS_SELECTOR)

    with open(f'exports/{board_name}.json', 'w', encoding='utf-8') as file:
        file.write(json_data.text)