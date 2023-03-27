from time import sleep

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

def get_card_evidences(card, driver):
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
        amount_downloads+=1
        driver.execute_script(f"""
            a = document.createElement('a');
            a.href = '{attachment['url']}';
            a.download = '{attachment['name']}';
            document.body.appendChild(a);
            a.click()
            document.body.removeChild(a);
            """
        )
    if amount_downloads: sleep(amount_downloads*1)
    return attachments

def is_card_with_tag(card, tag):
    return tag in get_card_labels(card)
