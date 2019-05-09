import flask as f
import netdrive
from ...util import login_required, file_getter
from .search import search
from .folder import down_folder, up_folder

net_bp = f.Blueprint('network', __name__)


@net_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    f.session["cur_folder"] = ''
    files, folders = file_getter(netdrive.app.config['UPLOAD_DIR'])
    return f.render_template('network/netdrive.html', files=files,
                             folders=folders, bread=f.session[
                                                        "cur_folder"].split("/")[
                                                    1:])


@net_bp.route('/search', methods=['GET', 'POST'])
@login_required
def search_route():
    return search()


@net_bp.route('/folder', methods=['GET', 'POST'])
@login_required
def folder_route():
    if f.request.args.get("up"):
        return up_folder()
    else:
        return down_folder()
