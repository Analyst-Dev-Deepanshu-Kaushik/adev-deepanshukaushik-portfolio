"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add project directory to the sys.path
path = '/home/ADevDeepanshuK/adev-deepanshukaushik-portfolio'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

# Import and run Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
