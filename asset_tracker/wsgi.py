"""
WSGI config for asset_tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

app_home = os.path.abspath(__file__).split('/')
app_home = app_home[:len(app_home)-3]
app_home = '/'.join(app_home)
paths = [app_home+'/asset_tracker']
for path in paths:
    if path not in sys.path:
        sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asset_tracker.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
