"""
Django settings for disqus_be project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, "disqus_be"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p9i0f+_ctqev7w)cmv#h!+e4mkn$-3rf2yjf!&%(!ynk(2opg9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

# AUTHENTICATION_BACKENDS = ('core_app.auth.GoogleBackend','django.contrib.auth.backends.ModelBackend')
# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_URL = '/logout/'
# OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'

GOOGLE_OAUTH2_CLIENT_ID = '223596340449-m956tumglqlhmtbvvjvi707j3ud81rl8.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'MMUmB2nIzAJ1KdK1ti-Runa6'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.staticfiles',
    # 'social_auth',
    # 'provider',
    # 'provider.oauth2', # pip install django-oauth2-provider
    'tastypie',
    'core_app',
    )

# STATIC_ROOT = ''
# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )

# TEMPLATE_DIRS = (
#     BASE_DIR + '/disqus_be/templates/',
# )

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# #     'django.template.loaders.eggs.Loader',
# )

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'disqus_be.urls'

WSGI_APPLICATION = 'disqus_be.wsgi.application'

SQLITE_URL = os.environ.get(
    'SQLITE_URL', os.path.join(BASE_DIR, 'db.sqlite3'))

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SQLITE_URL,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

TEST_RUNNER = "djnose2.TestRunner"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.stripe.StripeBackend',
    'social_auth.backends.steam.SteamBackend',
    'social_auth.backends.reddit.RedditBackend',
    'social_auth.backends.amazon.AmazonBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.flickr.FlickrBackend',
    'social_auth.backends.contrib.instagram.InstagramBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.yandex.YandexBackend',
    'social_auth.backends.contrib.yandex.YandexOAuth2Backend',
    'social_auth.backends.contrib.yandex.YaruBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.douban.DoubanBackend',
    'social_auth.backends.contrib.vk.VKOpenAPIBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.contrib.odnoklassniki.OdnoklassnikiBackend',
    'social_auth.backends.contrib.odnoklassniki.OdnoklassnikiAppBackend',
    'social_auth.backends.contrib.mailru.MailruBackend',
    'social_auth.backends.contrib.dailymotion.DailymotionBackend',
    # 'social_auth.backends.contrib.shopify.ShopifyBackend',
    # 'social_auth.backends.contrib.exacttarget.ExactTargetBackend',
    'social_auth.backends.contrib.stocktwits.StocktwitsBackend',
    'social_auth.backends.contrib.behance.BehanceBackend',
    'social_auth.backends.contrib.readability.ReadabilityBackend',
    'social_auth.backends.contrib.fedora.FedoraBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.request',
#     'social_auth.context_processors.social_auth_by_name_backends',
# )

# LOGIN_REDIRECT_URL = '/'

# import random
# # If doesn't get than we could generate
# SOCIAL_AUTH_DEFAULT_USERNAME = lambda: random.choice(['Darth_Vader', 'Obi-Wan_Kenobi', 'R2-D2', 'C-3PO', 'Yoda'])
# # Permit create users through social_auth
# SOCIAL_AUTH_CREATE_USERS = True

# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social_auth.backends.pipeline.social.social_auth_user',
#     'social_auth.backends.pipeline.associate.associate_by_email',
#     'social_auth.backends.pipeline.misc.save_status_to_session',
#     'app.pipeline.redirect_to_form',
#     'app.pipeline.username',
#     'social_auth.backends.pipeline.user.create_user',
#     'social_auth.backends.pipeline.social.associate_user',
#     'social_auth.backends.pipeline.social.load_extra_data',
#     'social_auth.backends.pipeline.user.update_user_details',
#     'social_auth.backends.pipeline.misc.save_status_to_session',
#     'app.pipeline.redirect_to_form2',
#     'app.pipeline.first_name',
# )

# try:
#     from example.local_settings import *
# except Exception as e:
#     pass
