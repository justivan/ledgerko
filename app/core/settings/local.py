# ruff: noqa: E501
import socket

from .base import *  # noqa: F403
from .base import INSTALLED_APPS, MIDDLEWARE, env

# general
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="1lWW4z4nKHGEnKEanHQmzXLFr1WvUmYu90zmliRZHEet4MV5Vgenifn58IQxGoo7",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]  # noqa: S104

# whitenoise
INSTALLED_APPS = ["whitenoise.runserver_nostatic", *INSTALLED_APPS]

# django-debug-toolbar
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = ["127.0.0.1"] + [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# django-extensions
INSTALLED_APPS += ["django_extensions"]
