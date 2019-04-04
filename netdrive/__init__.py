# TODO: Split file up into classes and into respective modules files
import flask as f
import os
from netdrive.modules import auth, network
from netdrive.util import url_check

app = f.Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config["SECRET_KEY"]

# <editor-fold desc="Description">
app.register_blueprint(auth.auth_bp, url_prefix='/auth')
app.register_blueprint(network.net_bp, url_prefix='/network')
# </editor-fold>


@app.route("/")
def index():
    return f.render_template("index.html", Failed=False)


# <editor-fold desc="Url handling">
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


# adds a timestamp to then end of a url to prevent caching
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return f.url_for(endpoint, **values)


@app.errorhandler(404)
def page_not_found(error):
    return f.render_template("codes/404.html"), 404
# </editor-fold>
