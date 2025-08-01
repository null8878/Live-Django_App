import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'replace-this-with-a-secure-key'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'blog',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'myproject.urls'
TEMPLATES = [{
    'BACKEND':'django.template.backends.django.DjangoTemplates',
    'DIRS':[os.path.join(BASE_DIR,'blog','templates')],
    'APP_DIRS':True,
    'OPTIONS':{'context_processors':[
        'django.template.context_processors.debug','django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages',
    ]},
}]
WSGI_APPLICATION = 'myproject.wsgi.application'
DATABASES = {
    'default':{'ENGINE':'django.db.backends.sqlite3','NAME':os.path.join(BASE_DIR,'db.sqlite3')}
}
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'blog','static')]
LOGIN_REDIRECT_URL = '/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
