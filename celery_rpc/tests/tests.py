"""
Force import of all modules in this package in order to get the standard test
runner to pick up the tests.  Yowzers.
"""

import os
import django

modules = [filename.rsplit('.', 1)[0]
           for filename in os.listdir(os.path.dirname(__file__))
           if filename.endswith('.py') and not filename.startswith('_')]
__test__ = dict()

if django.VERSION < (1, 6):
    for module in modules:
        exec("from celery_rpc.tests.%s import *" % module)