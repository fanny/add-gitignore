# -*- coding: utf-8 -*-

import requests
from util.file import *
from util.request import *
from util.response import *


def create_gitignore(languages):
    choices = get_all_templates()
    languages = ','.join([language.lower() for language in languages
                          if language.lower() in choices])
    if languages:
        data = _get_template_by_language(languages)
        write_file(data)
        response_sucess(languages)
    else:
        response_error()


def get_all_templates():
    url = '{base_url}/list'.format(base_url=BASE_URL)
    r = requests.get(url)
    return r.text


def _get_template_by_language(languages):
    url = '{base_url}/{lang}'.format(base_url=BASE_URL, lang=languages)
    r = requests.get(url)
    return r.text
