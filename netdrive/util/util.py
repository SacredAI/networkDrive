from functools import wraps
import flask as f


# Prevents Acessing the drive unless they are logged in
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if f.session['user'] is None:
            return f.redirect(f.url_for('index'))
        return func(*args, **kwargs)

    return decorated_function
