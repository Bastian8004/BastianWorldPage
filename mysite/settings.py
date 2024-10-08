import os
import posixpath
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #  ama być False na serwerze

ALLOWED_HOSTS = ['*','127.0.0.1','localhost','10.0','.pythonanywhere.com']

INSTALLED_APPS = [
    'captcha',
    'BW',
    'imagekit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites'
    ]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = '/admin/'

# Internationalization

LANGUAGE_CODE = 'pl-pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.8/howto/static-files/deployment/
# python manage.py collectstatic
#STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static/']))
STATIC_ROOT = BASE_DIR + '/static/'

MEDIA_URL = '/media/'
#MEDIA_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['media/']))
MEDIA_ROOT = BASE_DIR + '/media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'encoding': 'utf-8',  # Ustawienie kodowania na UTF-8
            'maxBytes': 1024 * 1024 * 3,  # Maksymalny rozmiar pliku 5 MB
            'backupCount': 3,  # Ilość kopii zapasowych
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
}






EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_USER')



STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME = "http://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True #
CSRF_COOKIE_SECURE = True #
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = True #
SECURE_FRAME_DENY = False
SECURE_BROWSER_XSS_FILTER = True  # Chroni przed atakami XSS
X_FRAME_OPTIONS = 'DENY'  # Zapobiega osadzaniu strony w ramkach (ochrona przed clickjackingiem)
SECURE_CONTENT_TYPE_NOSNIFF = True  # Ochrona przed atakami MIME type sniffing
SESSION_COOKIE_HTTPONLY = True  # Ogranicza dostęp do ciasteczek sesji z poziomu JavaScript
CSRF_COOKIE_HTTPONLY = True  # To samo dla ciasteczek CSRFsteczka sesji jako bezpieczne (tylko HTTPS)
SECURE_HSTS_PRELOAD = True  # Pozwala dodać witrynę do listy HSTS preload w przeglądarkach
