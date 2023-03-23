from selenium import webdriver
from controller import SeleniumController as sc
from controller import JsonController as jc
from selenium.webdriver.chrome.options import Options
import json

with open('config/app_config.json', 'r', encoding="utf-8") as json_file:
    config = json.load(json_file)

project = config['project']
tag = config['tag']

if config['check_trello'] == 'Y':
    if config['use_config_project_and_tag'] == 'N':
        project = input('Informe o Projeto que deseja buscar: ')
        tag = input('Informe a tag que deve ser consultada: ')

    options = Options()
    """
        # File download setup
        options.add_experimental_option("prefs", {
            "download.default_directory": r"C:\Development\Geral\rpa_for_trello_consumption",
            "download_restrictions": 0,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
    """
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    link = 'https://trello.com/'
    driver.get(link)

    sc.do_login(driver)
    sc.open_board(driver, project)
    sc.do_export(driver)
    
jc.read_json(tag)