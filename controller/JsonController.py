import os
import json
from io import TextIOWrapper
from utils import json_data as jr
from controller import DocumentController as dc
from docx import Document
from docx.document import Document as Doc

def read_json(project: str, tag: str, lists_to_get: list, relative_path_evidences: str, driver, full_path_evidences: str):
    relative_file_path = f'exports\\{project}.json'
    full_file_path = os.getcwd() + '\\' + relative_file_path
    
    if not os.path.isfile(full_file_path): 
        print(f'Não foi possível locallizar arquivo: {relative_file_path}')
        return
    
    with open(relative_file_path, 'r', encoding="utf-8") as json_file:
        board_info = json.load(json_file)
        board_info = build_board_info(board_info)
        cards_info = []

        for card in board_info['cards']:
            if not jr.is_valid_card(card, tag, lists_to_get, board_info): continue
            cards_info.append(build_card_info(card, board_info, driver, full_path_evidences))
    
    if not len(cards_info):
        print(f'Nenhum card encontrado com a tag: {tag} nas listas: {lists_to_get}!!!')
        return
    
    document: Doc = Document()
    for card_info in cards_info: add_card_info_doc(document, relative_path_evidences, card_info)
    document.save(f'Generated Documents/{project}_{tag}.docx')

def build_board_info(board_data):
    return {
        'members': jr.get_members(board_data),
        'checklists': jr.get_checklists(board_data),
        'lists': jr.get_lists(board_data),
        'cards': board_data['cards']
    }

def build_card_info(card, board_info, driver, full_path_evidences):
    return {
        'name': card['name'],
        'description': card['desc'],
        'members': jr.get_card_members(card, board_info['members']),
        'tags': jr.get_card_labels(card),
        'activities': jr.get_card_checklists(card, board_info['checklists']),
        'list': jr.get_card_list(card, board_info['lists']),
        'evidences': jr.get_card_evidences(card, driver, full_path_evidences)
    }

def add_card_info_doc(document: Doc, relative_path_evidences, card_info):
    dc.write_card_name(document, card_info["name"])
    dc.write_info_list(document, 'Membros', card_info['members'])
    dc.write_info_list(document, "Tags", card_info["tags"])
    dc.write_activities(document, card_info["activities"])
    dc.write_info(document, 'List', card_info["list"])
    dc.write_description(document, card_info['description'])
    dc.write_evidences(document, relative_path_evidences, card_info["evidences"])
    dc.write_blank_line(document)
