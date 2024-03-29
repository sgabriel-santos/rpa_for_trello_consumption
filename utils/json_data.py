from time import sleep
import os

def get_members(json_data):
    members = {}
    for member in json_data['members']:
        members[member['id']] = member
    return members

def get_checklists(json_data):
    checklists = {}
    for checklist in json_data['checklists']:
        checklists[checklist['id']] = checklist
    return checklists

def get_lists(json_data):
    lists = {}
    for list in json_data['lists']:
        lists[list['id']] = list
    return lists

def get_card_members(card, members):
    members_card = []
    for id_member in card["idMembers"]:
        members_card.append(members[id_member]['fullName'])
    return members_card

def get_card_checklists(card, checklists):
    checklists_card = []
    for id_checklist in card['idChecklists']:
        for item in checklists[id_checklist]['checkItems']:
            checklists_card.append({
                'name': item['name'],
                'state': item['state']    
            })
    return checklists_card

def get_card_list(card, lists):
    return lists[card['idList']]['name']

def get_card_labels(card):
    labels = []
    for label in card['labels']:
        labels.append(label['name'])
    return labels

def get_card_evidences(card, driver, full_path_evidences):
    amount_downloads = 0
    attachments = []
    for attachment in card['attachments']:
        if not attachment: continue
        if not attachment['name'].startswith('ev_'): continue
        
        attachments.append({
            'name': attachment['name'],
            'url': attachment['url']
        })
        
        #To download evidences
        if not driver: continue
        
        extension = attachment['url'].split('.')[-1]
        evidence_name = f"{attachment['name'].split('.')[0]}.{extension}"
        full_path_evidence = f"{full_path_evidences}\\{evidence_name}"
        if extension.lower() != 'png' and extension.lower() != 'jpeg': continue
        if os.path.isfile(full_path_evidence): continue
        
        amount_downloads+=1
        try:
            driver.execute_script(f"""
                a = document.createElement('a');
                a.href = '{attachment['url']}';
                a.download = '{attachment['name']}';
                document.body.appendChild(a);
                a.click()
                document.body.removeChild(a);
                """
            )
        except:
            print('Error downloading evidence:', evidence_name)
    if amount_downloads: sleep(amount_downloads*1)
    return attachments

def is_valid_card(card, tag, lists_to_get, board_info):
    return is_card_with_tag(card, tag) \
        and card_contains_any_list(card, lists_to_get, board_info) \
        and card['name'] != "CARD TEMPLATE"

def card_contains_any_list(card, lists_to_get, board_info):
    card_list = get_card_list(card, board_info['lists'])
    for list in lists_to_get:
        if card_list.find(list) != -1: return True
    return False


def is_card_with_tag(card, tag):
    return tag in get_card_labels(card)
