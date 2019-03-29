import flask as f
import json
import os
from passlib.hash import sha256_crypt
from werkzeug.utils import secure_filename

app = f.Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/store"


# <editor-fold desc="Authorisation">
@app.route("/")
def preauth():
    return f.render_template("index.html", failed=False)


@app.route("/auth", methods=["POST"])
def auth():
    if authcheck(f.request.form["user"], f.request.form["passw"]):
        return f.render_template_string("Yes")
    else:
        return f.render_template("index.html", failed=True)


# user check
def authcheck(username, password):
    with open('static/data/accounts.json') as r:
        data = json.load(r)
        for u in data['accounts']:
            if u['username'] == username:
                if sha256_crypt.verify(password, u['password']):
                    return True
    return False


# Setup Account for Access
def accountcreate(username, password):
    data = {}
    with open('static/data/accounts.json') as r:
        data = json.load(r)
        for u in data['accounts']:
            if u['username'] == username:
                return False

    with open('static/data/accounts.json', 'w') as w:
        data['accounts'].append({
            'username': username,
            'password': password
        })
        json.dump(data, w, indent=4)
    return True


# </editor-fold>


# <editor-fold desc="Url_for">
# Solves the issue where the browser loads cached static files instead of updated ones
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return f.url_for(endpoint, **values)


# </editor-fold>


app.run(debug=True)

# print(sha256_crypt.verify(password, password2))
