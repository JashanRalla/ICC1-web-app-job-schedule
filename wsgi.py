# makes a stable entrypoint for Gunicorn on Azure
try:
    from application import app  # if your Flask instance is named "app"
except ImportError:
    from application import application as app  # if it's named "application"
