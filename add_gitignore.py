# -*- coding: utf-8 -*-

import requests
import string

BASE_URL = 'https://api.github.com'


def write_file():
    with open('.gitignore', 'w') as f:
        data = get_template_by_language('c')['source']
        f.write(data)


def get_all_templates():
    """Get all gitignore templates available
        :return response: Json with templates
    """
    url = '{baseurl}/gitignore/templates'.format(baseurl=BASE_URL)
    headers = {'Accept': 'application/vnd.github.v3.raw+json'}
    r = requests.get(url, headers)
    return r.json()


def get_template_by_language(language):
    """Get the gitignore template specified,
        if not exists, None is returned, otherwise,
        a json.
        :return response: Json with specified template
    """
    language = string.capwords(language)
    url = '{baseurl}/gitignore/templates/{lang}'.format(baseurl=BASE_URL, lang=language)
    headers = {'Accept': 'application/vnd.github.v3.raw+json'}
    r = requests.get(url, headers)
    return r.json()


if __name__ == '__main__':
    write_file()


