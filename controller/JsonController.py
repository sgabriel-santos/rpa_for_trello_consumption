import os
import json
from io import TextIOWrapper
from utils import json_data as jr
from controller import DocumentController as dc
from docx import Document
from docx.document import Document as Doc

def read_json(project: str, tag: str, folder_evidences: str, driver):
    file_name = 'trello.json'
    file_path = os.getcwd() + '\\' + file_name
    
    if not os.path.isfile(file_path): 
        print(f'Não foi possível locallizar arquivo: {file_name}')
        return
    
    with open(file_name, 'r', encoding="utf-8") as json_file:
        board_info = json.load(json_file)
        board_info = build_board_info(board_info)
        cards_info = []

        for card in board_info['cards']:
            if not jr.is_card_with_tag(card, tag): continue
            cards_info.append(build_card_info(card, board_info, driver))
    
    with open('info.txt', 'w', encoding='utf-8') as txt_file:        
        document: Doc = Document()
        for card_info in cards_info:
            if card_info['name'] == "CARD TEMPLATE": continue
            add_card_info_txt(txt_file, card_info)
            add_card_info_doc(document, folder_evidences, card_info)
        document.save(f'{project}_{tag}.docx')

def build_board_info(board_data):
    return {
        'members': jr.get_members(board_data),
        'checklists': jr.get_checklists(board_data),
        'lists': jr.get_lists(board_data),
        'cards': board_data['cards']
    }

def build_card_info(card, board_info, driver):
    return {
        'name': card['name'],
        'description': card['desc'],
        'members': jr.get_card_members(card, board_info['members']),
        'tags': jr.get_card_labels(card),
        'activities': jr.get_card_checklists(card, board_info['checklists']),
        'list': jr.get_card_list(card, board_info['lists']),
        'evidences': jr.get_card_evidences(card, driver)
    }

def add_card_info_txt(txt_file: TextIOWrapper, card_info):
    txt_file.write('------\n')
    txt_file.write(f'Name: {card_info["name"]}\n')
    txt_file.write(f'Description: {card_info["description"]}')
    txt_file.write(f'Members: {card_info["members"]}\n')
    txt_file.write(f'Tags: {card_info["tags"]}\n')
    txt_file.write(f'Activities: {card_info["activities"]}\n')
    txt_file.write(f'List: {card_info["list"]}\n')
    txt_file.write(f'Evidences: {card_info["evidences"]}\n\n')

def add_card_info_doc(document: Doc, folder_evidences, card_info):
    dc.write_card_name(document, card_info["name"])
    dc.write_info(document, 'Membros', card_info['members'])
    dc.write_info(document, "Tags", card_info["tags"])
    dc.write_activities(document, card_info["activities"])
    dc.write_info(document, 'List', card_info["list"])
    dc.write_description(document, card_info['description'])
    dc.write_evidences(document, folder_evidences, card_info["evidences"])
    dc.write_blank_line(document)
