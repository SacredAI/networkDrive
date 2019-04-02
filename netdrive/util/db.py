import json


def create_and_update(tblname, keys, values):
    data = {}
    with open('netdrive/util/data/data.json') as j:
        data = json.load(j)

    if data[tblname] is not None:
        for i in range(keys.len()):
            temp = temp[keys[i]] = values[i]
            data[tblname].append(temp)
    else:
        data[tblname] = []
        for i in range(keys.len()):
            temp = temp[keys[i]] = values[i]
            data[tblname].append(temp)
    with open('netdrive/util/data/data.json') as j:
        json.dump(data, j, indent=4)


def read_data(tblname):
    tblname = str(tblname)
    data = {}
    with open('netdrive/util/data/data.json') as j:
        data = json.load(j)
    return data[tblname]
