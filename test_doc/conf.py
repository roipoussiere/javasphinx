#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A minimal configuration file for test purposes.

import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from javasphinx.apidoc import main as parse

parse(['', '-f', '-v', '-o', './javadoc', './src'])

extensions = ['javasphinx', 'sphinx.ext.todo']
master_doc = 'index'
project = 'Test doc'
author = 'Me'
copyright = '2016, ' + author
version = '1'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
todo_include_todos = True
