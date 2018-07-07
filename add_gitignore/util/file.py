# -*- coding: utf-8 -*-

FILE_NAME = '.gitignore'


def read_file():
    with open(FILE_NAME) as f:
        data = f.read()
    return data


def write_file(data):
    with open(FILE_NAME, 'a') as f:
        if not (data in read_file()):
            f.write(data)
