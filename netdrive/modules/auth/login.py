import flask as f
from ...util import read_data, url_check
from passlib.hash import sha256_crypt
from . import auth_bp


@auth_bp.route('/login', methods=['POST'])
def login():
    if auth_check(f.request.form["user"], f.request.form["passw"]):
        f.session['curuser'] = f.request.form['user']
        return f.render_template("network/netdrive.html")
    else:
        return f.render_template("index.html", Failed=True)

    # Auth Check


def auth_check(username, password):
    data = read_data('accounts')
    for u in data:
        if u['username'] == username:
            if sha256_crypt.verify(password, u['password']):
                return True
    return False
