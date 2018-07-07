# -*- coding: utf-8 -*-


def response_sucess():
    print "the gitignore template is generated"


def response_error(lang):
    print "The %s language specified is not writted because is not available " \
          "check more in: add_gitignore.py --help" % lang
