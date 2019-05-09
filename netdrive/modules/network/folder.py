import flask as f
import os
import netdrive
from ...util import file_getter


def down_folder():
    f.session["cur_folder"] = os.path.join(f.session["cur_folder"] + "/" +
                                           f.request.args.get('fol'))
    files, folders = file_getter(os.path.join(netdrive.app.config[
                                                  'UPLOAD_DIR'] + f.session[
                                                  "cur_folder"]))
    return f.render_template('network/netdrive.html', files=files,
                             folders=folders, bread=f.session[
                                                        "cur_folder"].split("/")[
                                                    1:])


def up_folder():
    f.session["cur_folder"] = f.session["cur_folder"].split('/')
    index = f.session["cur_folder"].index(f.request.args.get('fol'))
    f.session["cur_folder"] = "/".join(f.session["cur_folder"][:index + 1])
    files, folders = file_getter(os.path.join(netdrive.app.config[
                                                  'UPLOAD_DIR'] + f.session[
                                                  "cur_folder"]))
    return f.render_template('network/netdrive.html', files=files,
                             folders=folders, bread=f.session[
                                                        "cur_folder"].split("/")[
                                                    1:])
