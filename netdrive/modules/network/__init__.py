import flask as f
import netdrive
from ...util import login_required, file_getter
from .search import search

net_bp = f.Blueprint('network', __name__)


@net_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    files, folder = file_getter(netdrive.app.config['BASE_DIR'] +
                                "\\netdrive\\drive")
    return f.render_template('network/netdrive.html', files=files, folders=folder)


@net_bp.route('/search', methods=['GET', 'POST'])
@login_required
def search_route():
    return search()
