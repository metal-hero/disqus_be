"""This module contains url configuration.

Include your API resources and views into urlpatterns
"""
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from core_app.api import *
from django.contrib import admin
admin.autodiscover()

# from app.views import home, done, logout, error, form, form2, close_login_popup
# from app.facebook import facebook_view
# from app.vkontakte import vkontakte_view
# from app.odnoklassniki import ok_app, ok_app_info

v1_api = Api(api_name='v1')
v1_api.register(CommentResource())
v1_api.register(myUserResource())

urlpatterns = patterns(
    '',
    # url(r'^login/', 'core_app.api.login', name='login'),
    # url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    # url(r'^social/', include('social_auth.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

