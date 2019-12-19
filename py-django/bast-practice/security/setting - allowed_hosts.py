"""
Make sure, an appropriate host is set in ALLOWED_HOSTS, whenever DEBUG = False.
"""

""" settings.py """

DEBUG = False
# ...
ALLOWED_HOSTS = ['abc.com']
