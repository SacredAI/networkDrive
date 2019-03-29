import json

def jsonl(username, password):
    data = {}
    with open('static/data/accounts.json') as r:
        data = json.load(r)

    with open('static/data/accounts.json', 'w') as w:
        data['accounts'].append({
            'username': username,
            'password': password
        })
        json.dump(data, w, indent=4)


jsonl("sacred", "ajsfh")
