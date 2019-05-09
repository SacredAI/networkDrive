import flask as f
from ...util import file_getter
import netdrive


# TODO: Expand search to allow for matches if requested
def search():
    keyword = f.request.args.get("search")
    files, folders = file_getter(netdrive.app.config['UPLOAD_DIR'])
    fileresults = []
    folderresults = []
    for x in range(len(folders)):
        if keyword in folders[x]:
            folderresults.append(folders[x])
    for x in range(len(files)):
        if keyword in files[x]:
            fileresults.append(folders[x])
    return f.render_template("network/netdrive.html", files=fileresults,
                             folder=folderresults)
