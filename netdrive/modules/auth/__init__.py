import flask as f

auth_bp = f.Blueprint('auth', __name__, url_prefix='/auth/v1')
