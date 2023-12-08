"""
WSGI config for yourprojectname project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import sys
import os

path = '/home/elcot/prem/sitetest/site1/yourprojectname'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'yourprojectname.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

