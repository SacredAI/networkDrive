import flask as f
from ...util import read_data
from passlib.hash import sha256_crypt


def login():
    if auth_check(f.request.form["user"], f.request.form["passw"]) is True:
        f.session['user'] = f.request.form["user"]
        return f.redirect(f.url_for('network.index'))
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
    try:
        return sha256_crypt.verify(password, data.get('password'))
    except KeyError or TypeError:
        return False
