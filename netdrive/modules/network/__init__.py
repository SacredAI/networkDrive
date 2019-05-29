import os

import flask as f

import netdrive
from .folder import down_folder, up_folder
from .search import search
from ...util import login_required, file_getter
from .file import uploadfile, uploadfolder, download, rename, move, remove

net_bp = f.Blueprint('network', __name__)


# Base Drive page Can return home folder or subfolders
@net_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if f.request.args.get('home'):
        f.session["cur_folder"] = ''
        f.session['selected'] = ''
        f.session['folder'] = ''
    files, folders = file_getter(netdrive.app.config['UPLOAD_DIR'] +
                                 f.session["cur_folder"])
    f.g.search = False
    return f.render_template('network/netdrive.html', files=files,
                             folders=folders,
                             bread=f.session["cur_folder"].split("/")[1:])


@net_bp.route('/search', methods=['GET', 'POST'])
@login_required
def search_route():
    return search()


@net_bp.route('/upload/file', methods=['GET', 'POST'])
@login_required
def uploadfile_route():
    return uploadfile()


@net_bp.route('/upload/folder', methods=['GET', 'POST'])
@login_required
def uploadfolder_route():
    return uploadfolder()


@net_bp.route('/download', methods=['GET', 'POST'])
@login_required
def download_route():
    return download()


@net_bp.route('/folder', methods=['GET', 'POST'])
@login_required
def folder_route():
    if f.request.args.get("up"):
        return up_folder()
    else:
        return down_folder()


@net_bp.route('/parse', methods=['GET', 'POST'])
@login_required
def parse_route():
    f.session['selected'] = f.request.args.get('selected')
    return f.jsonify(result=True)


@net_bp.route('/rename', methods=['GET', 'POST'])
@login_required
def rename_route():
    return rename()


@net_bp.route('/move', methods=['GET', 'POST'])
@login_required
def move_route():
    return move()


@net_bp.route('/remove', methods=['GET', 'POST'])
@login_required
def remove_route():
    return remove()
