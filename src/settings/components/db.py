from src.settings.components import PROJECT_PATH


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_PATH + '\\db.sqlite3',
    }
}