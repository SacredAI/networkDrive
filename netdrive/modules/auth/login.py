import flask as f
from ...util import read_data
from passlib.hash import sha256_crypt


def login():
    if auth_check(f.request.form["user"], f.request.form["passw"]) is True:
        f.g.user = f.request.form["user"]
        return f.render_template("network/netdrive.html")
    else:
        return f.render_template("index.html", Failed=True)

    # Auth Check


def auth_check(username, password):
    '''
    :param str username: The username used during the login process
    :param str password: The password used during the login process
    :return: returns a failed or passed result
    :rtype: boolean
    '''
    data = read_data('accounts', username)
    for u in data.keys():
        if data[u] == username:
            if sha256_crypt.verify(str(password), str(data['password'])):
                return True
    return False

