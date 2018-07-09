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
    """Write in gitignore file, using append mode,
    namely, whenever new information
    is passed is inserted at the end,
    if the information already exists
    in the file will not be inserted.
    :param data: the data to be insert in gitignore file
    """
    with open(FILE_NAME, 'a') as f:
        if not (data in read_file()):
            f.write(data)
