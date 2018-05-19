import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=simbion'
        },
        'NAME': os.environ.get('DB_NAME', 'dummy'),
        'USER': os.environ.get('DB_USER', 'dummy'),
        'PASSWORD': os.environ.get('DB_PASS','dummy'),
        'HOST': os.environ.get('DB_HOST', 'cs.ui.ac.id'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
