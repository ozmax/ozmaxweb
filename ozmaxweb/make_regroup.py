import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ozmaxweb.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import django
django.setup()
populate()
from blog.models import Post
