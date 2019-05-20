import os

import flask as f

import netdrive
from ...util import upload_file, upload_folder


def uploadfile():
    if f.request.method == 'POST':
        for key, files in f.request.files.items():
            if key.startswith('file'):
                upload_file(files,
                            os.path.join(netdrive.app.config[
                                             'UPLOAD_DIR'] +
                                         f.session[
                                             'cur_folder']))
    return f.redirect(f.url_for('network.index', home=False))


def uploadfolder():
    if f.request.method == "POST":
        for x in f.request.files.getlist("folderupload"):
            upload_folder(x,
                          os.path.join(netdrive.app.config[
                                           'UPLOAD_DIR'] +
                                       f.session[
                                           'cur_folder']))

    return f.redirect(f.url_for('network.index', home=False))


def download():
    if f.session['selected']:
        return f.send_file(os.path.join(netdrive.app.config['UPLOAD_DIR'],
                                        f.session['cur_folder'],
                                        f.session['selected']), as_attachment=True)
    return f.redirect(f.url_for('network.index', home=False))
