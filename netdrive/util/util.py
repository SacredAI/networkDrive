from . import read_data
import json


def url_check(user, adminpg):
    if user is None:
        return False
    elif adminpg:
        data = None
        with open('netdrive/util/data/data.json') as j:
            data = json.load(j)
        for u in data['accounts']:
            if u['username'] == user:
                perms = u['perms']
                for p in perms:
                    if p == '*':
                        return True
                    else:
                        # TODO: Finish permissions setup
                        return False
    else:
        return True
