# -*- coding: utf-8 -*-


def response_sucess(languages):
    """Creates a sucess response that indicates the gitignore is generated
    """
    print "Added .gitignore for {languages}".format(languages=languages)


def response_error():
    """Creates a error response that indicates the language was not writted
    :param lang: the languages was not be writted in gitignore file
    """
    print "The language specified is not writted because is not available check more in: add_gitignore.py --help"
