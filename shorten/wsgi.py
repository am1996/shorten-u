import os
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shorten.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
