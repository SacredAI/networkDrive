import flask as f


def down_folder():
    f.session["cur_folder"] = f.session["cur_folder"] \
                              + '/' + f.request.args.get('fol')
    return f.redirect(f.url_for('network.index'))


def up_folder():
    f.session["cur_folder"] = f.session["cur_folder"].split('/')
    index = f.session["cur_folder"].index(f.request.args.get('fol'))
    f.session["cur_folder"] = "/".join(f.session["cur_folder"][:index + 1])
    return f.redirect(f.url_for('network.index'))
