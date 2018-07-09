# -*- coding: utf-8 -*-


def response_sucess():
    """Creates a sucess response that indicates the gitignore is generated
    """
    print "the gitignore template is generated"


def response_error(lang):
    """Creates a error response that indicates the language was not writted
    :param lang: the languages was not be writted in gitignore file
    """
    print "The %s language specified is not writted because is not available " \
          "check more in: add_gitignore.py --help" % lang
