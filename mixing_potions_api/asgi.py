import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mixing_potions_api.settings')

application = get_asgi_application()
