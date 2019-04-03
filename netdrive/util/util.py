
from . import read_data
import json


def url_check(user, adminpg):
    '''
    :param user: The username of the client trying to load the page
    :type user: str or None
    :param adminpg: Does the page require elevated privileges
    :type adminpg: bool
    :return: Failed or passed
    :rtype: bool
    '''
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
