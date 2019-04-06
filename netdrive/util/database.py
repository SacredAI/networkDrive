from flask import json
import os, sys

# Apparently I can't import app into here so were doing this instead
base_dir = os.path.dirname(os.path.realpath(sys.argv[0]))


def create_and_update(table, dataset, keys, values):
    '''
    :param table: Name of the Table being accessed
    :type table: str
    :param dataset: dataset being accessed
    :type dataset: str
    :param keys: All the keys used to identify values in the corresponding position
    :type keys: list
    :param values: All the vales identified by its key in the corresponding position
    :type values: list
    :return: nil
    :raises IndexError: Raised if the function is passed an empty list
    '''
    if keys[0] is None or values[0] is None:
        raise IndexError('You passed an empty list')
    data = {}
    with open(os.path.join(base_dir, 'netdrive/util/data/data.json')) as j:
        data = json.load(j)
    if table not in data:
        data[table] = {}
    if dataset not in data[table]:
        data[table][dataset] = {}
    for i in range(len(keys)):
        data[table][dataset][keys[i]] = values[i]
    with open(os.path.join(base_dir, 'netdrive/util/data/data.json'), 'w') as j:
        json.dump(data, j, indent=4)


def read_data(table, dataset):
    '''
    :param table: Name of the table to Access
    :type table: str
    :param dataset: Name of Dataset to Access
    :type dataset: str
    :return: Returns the table specified
    :rtype: dict
    :raises: IOError
    '''
    data = {}
    with open(os.path.join(base_dir, 'netdrive/util/data/data.json')) as j:
        data = json.load(j)
    if table in data or dataset in data[table]:
        return data[table][dataset]
    else:
        return {}
