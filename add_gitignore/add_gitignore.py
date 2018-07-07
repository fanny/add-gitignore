# -*- coding: utf-8 -*-

import requests
import string
from util.file import *
from util.request import *
from util.response import *


def create_gitignore(languages):
    size = len(languages)
    choices = get_all_templates()
    index = 0
    while index < size-1 and languages[index] in choices:
        data = _get_template_by_language(languages[index])
        write_file(data['source'])

    if index == size:
        response_sucess()
    else:
        response_error(languages[index])


def get_all_templates():
    r = requests.get(SEARCH_URL, HEADER)
    return r.json()


def _get_template_by_language(language):
    language = string.capwords(language)
    url = '{base_url}/{lang}'.format(base_url=SEARCH_URL, lang=language)
    r = requests.get(url, HEADER)
    return r.json()
