import os
from .. import app
from werkzeug.utils import secure_filename

import flask as f

base_dir = app.config['BASE_DIR']


def _file_check(file, path):
    if file is None:
        raise FileNotFoundError('Couldn\'t find the File you specified')
    if path is None or not os.path.exists(path):
        raise NotADirectoryError('Couldn\'t find the Folder you specified')
    return


def upload_file(file, path):
    _file_check(file, path)
    file = secure_filename(file.filename)
    file.save(os.path.join(path, file.filename))
    return f.redirect(f.url_for(
        'network.index'))  # Change this to some javascript/restapi/ Ajax stuff
    # so I don't need to reload


def delete_file(file, path):
    _file_check(file, path)
    file = secure_filename(file.filename)
    os.remove(os.path.join(path, file.filename))
    return f.redirect(f.url_for('network.index'))


def rename_file(file, path, newname):
    _file_check(file, path)
    newname = secure_filename(newname)
    os.rename(os.path.join(path, file), os.path.join(path, newname))
    return f.redirect(f.url_for('network.index'))


def create_folder(basepath, folder):
    if not os.path.exists(basepath):
        raise NotADirectoryError('Couldn\'t find the folder you specified')
    folders = folder.split('/')
    if len(folders) <= 2:
        os.makedirs(os.path.join(basepath, folder))
    else:
        t = ''
        for x in range(len(folders)):
            if x != '/':
                if os.path.exists(os.path.join(basepath, folders[x - x + 1])):
                    basepath = os.path.join(basepath, folders[x - x + 1])
                else:
                    t = os.path.join(t, folders[x - x + 1])
    return f.redirect(f.url_for('network.index'))


def delete_folder(path):
    if not os.path.exists(path):
        raise NotADirectoryError('Couldn\'t find the folder specified')
    os.remove(path)
    f.redirect(f.url_for('network.index'))