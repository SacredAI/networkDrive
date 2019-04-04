import flask as f
from .login import login

auth_bp = f.Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login_route():
    return login()
