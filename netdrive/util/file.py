import os
from werkzeug.utils import secure_filename
import flask as f
import netdrive


def _file_check(file, path):
    '''
    :param File file: File to check
    :param str path: Path to check
    :return: Failed or Passed
    :rtype: bool
    :raises FileNotFoundError:
    :raises NotADirectoryError:
    '''
    if file is None:
        raise FileNotFoundError('Couldn\'t find the File you specified')
    if path is None or not os.path.exists(path):
        raise NotADirectoryError('Couldn\'t find the Folder you specified')
    return


def upload_file(file, path):
    '''
    :param File file: File to upload
    :param str path: Directory to upload to
    '''
    for x in range(len(netdrive.app.config["BLOCKED_EXT"])):
        if netdrive.app.config["BLOCKED_EXT"][x] in file.filename:
            f.g.blockedext = netdrive.app.config["BLOCKED_EXT"][x]
            return
    file.save(os.path.join(path, secure_filename(file.filename)))


def upload_folder(file, path):
    '''
        :param File file: current File bing uploaded
        :param str path: Directory to upload to
    '''
    for x in range(len(netdrive.app.config["BLOCKED_EXT"])):
        if netdrive.app.config["BLOCKED_EXT"][x] in file.filename:
            f.g.blockedext = netdrive.app.config["BLOCKED_EXT"][x]
            return
    folder = file.filename.split("/")
    folder = '/'.join(folder[:len(folder) - 1])
    if not os.path.exists(os.path.join(path, folder)):
        create_folder(path, folder)
    file.save(os.path.join(path, folder, secure_filename(file.filename)))


def delete_file(file, path):
    '''
    :param File file: File to be deleted
    :param str path: Path to the file
    '''
    _file_check(file, path)
    file = secure_filename(file)
    os.remove(os.path.join(path, file))
    return f.redirect(f.url_for('network.index'))


def rename_file(file, path, newname):
    '''
    :param File file: file to be renamed
    :param str path: path the to the file
    :param str newname: The Replacement Name
    '''
    _file_check(file, path)
    newname = secure_filename(newname)
    os.rename(os.path.join(path, file.filename), os.path.join(path, newname))


def create_folder(basepath, folder):
    '''
    :param str basepath: Path to where the folder should be created
    :param str folder: Folder to create
    '''
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


def delete_folder(path):
    '''
    :param str path: Path to the folder where the last folder is the one being
    removed
    '''
    if not os.path.exists(path):
        raise NotADirectoryError('Couldn\'t find the folder specified')
    # Empties a folder before deleting it because python can't delete a folder if it
    # has files inside
    for root, folders, files in os.walk(path, topdown=False):
        for x in files:
            os.remove(os.path.join(root, x))
        for x in folders:
            os.rmdir(os.path.join(root, x))
    os.rmdir(path)


def file_getter(path):
    '''
    :param str path: Path to the base folder to check
    :return: List of Files and Folders
    '''
    files = []
    folders = []
    for root, folder, file in os.walk(path):
        if root != path:
            break
        for x in file:
            files.append(x)
        for x in folder:
            folders.append(x)
    return files, folders
