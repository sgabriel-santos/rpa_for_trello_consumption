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

def is_card_with_tag(card, tag):
    return tag in get_card_labels(card)
