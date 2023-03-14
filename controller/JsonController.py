import json
from utils import json_data as jr

def read_json(tag: str):
    with open('trello.json', 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
        members = jr.get_members(data)
        checklists = jr.get_checklists(data)
        lists = jr.get_lists(data)
        
        with open('info.txt', 'w', encoding='utf-8') as file_info:
            for card in data['cards']:
                if not jr.is_card_with_tag(card, tag): continue
                file_info.write('------\n')
                file_info.write(f'Name: {card["name"]}\n')
                file_info.write(f'Members: {jr.get_card_members(card, members)}\n')
                file_info.write(f'Tags: {jr.get_card_labels(card)}\n')
                file_info.write(f'Activities: {jr.get_card_checklists(card, checklists)}\n')
                file_info.write(f'List: {jr.get_card_list(card, lists)}\n\n')