from selenium import webdriver
from controller import SeleniumController as sc
from controller import JsonController as jc
from controller import DocumentController as dc
from selenium.webdriver.chrome.options import Options
import json
import os

EVIDENCES_DIR = f'{os.getcwd()}\\evidences'
EXPORTS_DIR = f'{os.getcwd()}\\exports'
GENERETED_DOCS_DIR = f'{os.getcwd()}\\Generated Documents'

with open('config/app_config.json', 'r', encoding="utf-8") as json_file:
    config = json.load(json_file)

project = config['project']
tag = config['tag']
driver = None

if not os.path.isdir(EVIDENCES_DIR): os.mkdir(EVIDENCES_DIR)
if not os.path.isdir(EXPORTS_DIR): os.mkdir(EXPORTS_DIR)
if not os.path.isdir(GENERETED_DOCS_DIR): os.mkdir(GENERETED_DOCS_DIR)

if config['check_trello'] == 'Y':
    if config['use_config_project_and_tag'] == 'N':
        project = input('Informe o Projeto que deseja buscar: ')
        tag = input('Informe a tag que deve ser consultada: ')

    # File download setup
    options = Options()
    full_path_evidences = f"{os.getcwd()}\\evidences\\{project}_{tag}"
    options.add_experimental_option("prefs", {
        "download.default_directory": full_path_evidences,
        "download_restrictions": 0,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
    })
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    link = 'https://trello.com/login'
    driver.get(link)

    sc.do_login(driver)
    sc.do_export(driver, project, tag)

relative_path_evidences = f"evidences/{project}_{tag}"
jc.read_json(project, tag, relative_path_evidences, driver, full_path_evidences)
