from functools import wraps
import flask as f


# TODO: set this up
def permissions_check(user, path):
    '''
    :param user: Username of the user trying to access the page
    :type user: str
    :param path: Path to the file/page they are trying to access
    :type path: str
    :return: Failed or Passed
    :rtype: bool
    '''
    return


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if f.session['user'] is None:
            return f.redirect(f.url_for('index'))
        return func(*args, **kwargs)

    return decorated_function
