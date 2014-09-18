"""
Django settings for MiniFlash project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(c4_!j&(5-$k08b@qcjdoed!lz#w%xb^_ddxjp0ul5*ou@u6sq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	'allauth',
	'allauth.account',
	'south',
	'User',
	'bootstrap3',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MiniFlash.urls'

WSGI_APPLICATION = 'MiniFlash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'miniflash_database',
		'USER': 'postgresuser',
		'PASSWORD': 'postgres',
		'HOST': '127.0.0.1',
		'PORT': '5432',
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Ljubljana'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
	# Required by allauth template tags
	"django.core.context_processors.request",
	# allauth specific context processors
	"allauth.account.context_processors.account",
	"allauth.socialaccount.context_processors.socialaccount",
	'django.contrib.auth.context_processors.auth',
)

AUTHENTICATION_BACKENDS = (
	# Needed to login by username in Django admin, regardless of `allauth`
	"django.contrib.auth.backends.ModelBackend",
	# `allauth` specific authentication methods, such as login by e-mail
	"allauth.account.auth_backends.AuthenticationBackend",
)

# AllAuth
AUTH_USER_MODEL = 'User.CustomUser'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SOCIALACCOUNT_AUTO_SIGNUP = False
ACCOUNT_FORMS = {'login': 'User.forms.CustomLoginForm', 'signup': 'User.forms.CustomSignupForm'}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Default settings
BOOTSTRAP3 = {
	# The URL to the jQuery JavaScript file
	'jquery_url': os.path.join(BASE_DIR, 'static/js/jquery-2.1.1.min.js'),

	# The complete URL to the Bootstrap CSS file (None means derive it from base_url)
	'css_url': os.path.join(BASE_DIR, 'static/css/bootstrap.css'),

	# The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
	'javascript_url': os.path.join(BASE_DIR, 'static/js/bootstrap.js'),
}