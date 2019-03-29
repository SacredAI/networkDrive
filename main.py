import flask as f
import json
from passlib.hash import sha256_crypt
from werkzeug.utils import secure_filename

app = f.Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/store"


@app.route("/")
def preauth():
    return f.render_template("index.html")


@app.route("/auth", methods=["POST"])
def auth():
    return


def items():
    return

# user check
def authcheck(username, password):
    with open('static/data/accounts.json') as r:
        data = json.load(r)
        for u in data['accounts']:
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


app.run(debug=True)

# print(sha256_crypt.verify(password, password2))
