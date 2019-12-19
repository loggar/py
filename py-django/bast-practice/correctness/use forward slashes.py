"""
Django requires you to use forward slashes / whenever you indicate a path, even on Windows. In your settings, this is true for the following variables.

STATICFILES_DIRS
TEMPLATE_DIRS
DATABASES['<your database>'][NAME]
FIXTURE_DIRS

Anti-pattern:

STATICFILES_DIRS = [
    "\\path\\to\\my\\static\\files",
]
"""

""" settings.py """

STATICFILES_DIRS = [
    "/path/to/my/static/files",
]
