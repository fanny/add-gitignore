# -*- coding: utf-8 -*-

import requests
import string
import argparse

SEARCH_URL = 'https://api.github.com/gitignore/templates'
HEADER = {'Accept': 'application/vnd.github.v3.raw+json'}
FILE_NAME = '.gitignore'


def write_file(data):
    with open(FILE_NAME, 'a') as f:
        f.write(data)


def get_all_templates():
    """Get all gitignore templates available
        :return response: Json with templates
    """
    r = requests.get(SEARCH_URL, HEADER)
    return r.json()


def get_template_by_language(language):
    """Get the gitignore template specified,
        if not exists, None is returned, otherwise,
        a json.
        :return response: Json with specified template
    """
    language = string.capwords(language)
    url = '{base_url}/{lang}'.format(base_url=SEARCH_URL, lang=language)
    r = requests.get(url, HEADER)
    return r.json()


def get_parser():
    parser = argparse.ArgumentParser(description='Generate Gitignore rules basing on GitHub"s templates collection')
    parser.add_argument("-l", "--language", help="Get the gitignore template specified", nargs='+')
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if args['language']:
        for language in args['language']:
            data = get_template_by_language(language)
            write_file(data['source'])
    else:
        parser.print_help()


if __name__ == '__main__':
    command_line_runner()


