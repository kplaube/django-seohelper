DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
}
SECRET_KEY = "dsl"
INSTALLED_APPS = ["django.contrib.sites", "django.contrib.flatpages", "seohelper"]
MIDDLEWARE_CLASSES = []
