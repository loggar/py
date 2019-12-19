"""
TEMPLATE_DEBUG = True
"""

""" settings.py """

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': '/path/to/my/templates',
        'OPTIONS': {
            'debug': True,
        }
    },
]
