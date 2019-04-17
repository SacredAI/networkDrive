import flask as f
import netdrive
from ...util import login_required, file_getter

net_bp = f.Blueprint('network', __name__)


@net_bp.route('/')
@login_required
def index():
    files, folder = file_getter(netdrive.app.config['BASE_DIR'] + "\\netdrive\\drive")
    print(files)
    print(folder)
    return f.render_template('network/netdrive.html', files=files, folders=folder)
