from django.contrib import admin
from django.contrib.auth.models import User, Group
from core_app.models import *

admin.site.register(Comment)
admin.site.unregister(User)
admin.site.unregister(Group)
