from selenium import webdriver
from controller import SeleniumController as sc
from controller import JsonController as jc
import json

with open('config/app_config.json', 'r', encoding="utf-8") as json_file:
    config = json.load(json_file)

project = config['project']
tag = config['tag']

if config['check_trello'] == 'Y':
    if config['use_config_project_and_tag'] == 'N':
        project = input('Informe o Projeto que deseja buscar: ')
        tag = input('Informe a tag que deve ser consultada: ')

    driver = webdriver.Chrome()
    driver.create_options()
    driver.maximize_window()
    link = 'https://trello.com/'
    driver.get(link)

    sc.do_login(driver)
    sc.open_board(driver, project)
    sc.do_export(driver)
    driver.close()
    
jc.read_json(tag)