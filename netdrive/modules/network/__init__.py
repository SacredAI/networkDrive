import flask as f
from ...util import login_required

net_bp = f.Blueprint('network', __name__)


@net_bp.route('/')
@login_required
def index():
    return f.render_template('network/netdrive.html')
