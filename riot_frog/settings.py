# Django settings for riot_frog project.
# We will use chef to deploy settings in local_settings.py
# This file merely imports that

try:
    from local_settings import *
except ImportError:
    pass
