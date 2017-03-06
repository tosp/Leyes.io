#!/usr/bin/env python

import fileinput
import os
import sys


filesToEdit = ['HOWTOUSE.md',
               'manage.py',
               'docs/djangoTemplate.rst',
               'djangoTemplate/urls.py',
               'djangoTemplate/wsgi.py',
               'djangoTemplate/settings/base.py']

with fileinput.FileInput(filesToEdit, inplace=True) as file:
    for line in file:
        print(line.replace('djangoTemplate', sys.argv[1]), end='')


# Change the name of the main project folder
os.rename('djangoTemplate', sys.argv[1])
