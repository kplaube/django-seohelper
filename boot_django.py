# File sets up the django environment, used by other scripts that need to
# execute in Django land
import sys
from pathlib import Path
import django
from django.conf import settings

BASE_DIR = Path(__file__).parent
sys.path.insert(0, str(BASE_DIR))


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default":{
                "ENGINE":"django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=(
            "django.contrib.sites",
            "django.contrib.flatpages",
            "seohelper",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )
    django.setup()