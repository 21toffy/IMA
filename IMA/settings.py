
import os
import django_heroku 
# import cloudinary
import warnings


warnings.filterwarnings("ignore", message="No directory at", module="whitenoise.base" )


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0hhl=p^aby&!)v#i$giipjd*pshxs+$tn!3*b#&ws!128d_bak'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['influencemediaafrica.herokuapp.com', '127.0.0.1', 'influencemediaafrica.com']

# Application definition

INSTALLED_APPS = [
    'paystack',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'paystack',
    # 'cloudinary',
    'blog',
    'controlpanel',
    'core',
    'courses',
    'newsletters',
    'users',
    'django_sass',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IMA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'IMA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# cloudinary.config( 
#   cloud_name = "toffy", 
#   api_key = "393415259869955", 
#   api_secret = "XISdAJ5DC6g01zRqpZxxWrYZnVs" 
# )



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False

SITE_ID = 1

# To reconfigure the production database
import dj_database_url

prod_db  =  dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(prod_db)


MAILCHIMP_API_KEY='c2b6d9fd7d1c079cda81ec7e4c04d93c-us17'
MAILCHIMP_DATA_CENTER = 'us17'
MAILCHIMP_EMAIL_LIST_ID=''

PAYSTACK_PUBLIC_KEY  = 'pk_test_9770b7b9d5a982da69a8a4e8b757b1cebf4e1eac'
PAYSTACK_SCRET_KEY  = 'sk_test_4db78b22173f2be5815b028ef008bd8dce69004e'

EMAIL_HOST='smtp.gmail.com'

EMAIL_HOST_USER='tosdoltos@gmail.com'
EMAIL_HOST_PASSWORD='0Luw@t0funm1'
EMAIL_PORT=587
EMAIL_USE_TLS= True