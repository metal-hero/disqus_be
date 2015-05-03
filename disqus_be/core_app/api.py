"""This module contains API resource classes"""
from tastypie.resources import ModelResource
# from core_app.models import Comment
from tastypie.authorization import Authorization
from tastypie import fields
from core_app import utils
# from provider.oauth2.forms import AuthorizationForm
import json
from django.http import HttpResponse

from core_app.models import Comment,myUser
from core_app import utils
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


# Mr.German I tried many times to use some libraries for Google authorization
# And nothing works. Some libraries doesn't work with Django 1.7 or another
# strange error
# And now I'll realize own registration.

# def login(request):
#     # authorization_form = AuthorizationForm()
#     # g = authorization_form.save()
#     # print q
#     response_data = {}
#     response_data['result'] = 'failed'
#     response_data['message'] = 'You messed up'
#     return HttpResponse(json.dumps(response_data), content_type="application/json")

class myUserResource(ModelResource):
    name = fields.CharField(attribute="name")
    email = fields.CharField(attribute="email")
    password = fields.CharField(attribute="password")

    class Meta:
        queryset = myUser.objects.all()
        resource_name = 'my_user'
        excludes = ['password']
        authorization = Authorization()
        always_return_data = True

    # def hydrate(self, bundle):
    #     if bundle.request.method == 'POST':
    #         print bundle.data
    #         # bundle.obj.pk = bundle.data['pk']
    #         bundle.data['name'], bundle.data['surname'] = bundle.data['name'][0].upper(
    #         ) + bundle.data['name'][1:], bundle.data['surname'][0].upper() + bundle.data['surname'][1:]
    #         bundle.obj.name, bundle.obj.surname = bundle.data[
    #             'name'], bundle.data['surname']
    #         bundle.obj.phone = bundle.data['phone']
    #         bundle.obj.email = bundle.data['email']
    #         Secretary.refreshUser(bundle.obj)
    #         info = {'text': "You have created " + unicode(bundle.obj) + "!",
    #                 'info': {'login': bundle.obj.login, 'password': bundle.obj.password}}
    #         bundle.obj.save()
    #         send_mail_to_student(info, bundle.obj)
    #         print "New student was successfully added!"
    #     return bundle


class CommentResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        filtering = {
            # 'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
