# -*- coding: utf-8 -*-

FILE_NAME = '.gitignore'


def read_file():
    """Read gitignore file and return its data.
    :return: gitignore data
    """
    with open(FILE_NAME) as f:
        data = f.read()
    return data


def write_file(data):
    """Write in gitignore file
    :param data: the data to be insert in gitignore file
    """
    with open(FILE_NAME, 'w') as f:
        if not (data in read_file()):
            f.write(data)
