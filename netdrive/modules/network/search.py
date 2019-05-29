import os

import flask as f
import netdrive


def search():
    keyword = f.request.args.get("search")
    files, folders = directory_walk(netdrive.app.config['UPLOAD_DIR'])
    fileresults = []
    folderresults = []
    for x in range(len(folders)):
        if keyword in folders[x]:
            folderresults.append(folders[x])
    for x in range(len(files)):
        if keyword in files[x]:
            fileresults.append(folders[x])
    f.g.search = True
    return f.render_template("network/netdrive.html", files=fileresults,
                             folders=folderresults)


def directory_walk(path):
    '''
    :param str path: Path to the base folder to check
    :return: List of Files and Folders
    '''
    files = []
    folders = []
    for root, folder, file in os.walk(path):
        for x in file:
            files.append(x)
        for x in folder:
            folders.append(x)
    return files, folders
