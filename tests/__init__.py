import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.core.settings")
django.setup()
