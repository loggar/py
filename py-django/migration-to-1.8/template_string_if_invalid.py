"""
TEMPLATE_STRING_IF_INVALID = 'Invalid variable'
"""

""" settings.py """

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': '/path/to/my/templates',
        'OPTIONS': {
            'string_if_invalid': 'Invalid varialbe!',
        }
    },
]
