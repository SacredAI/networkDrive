import flask as f

net_bp = f.Blueprint('network', __name__, template_folder='templates')


@net_bp.route('/')
def index():
    return f.render_template('network/netdrive.html')
