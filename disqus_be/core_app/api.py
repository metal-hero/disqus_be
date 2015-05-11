"""This module contains API resource classes"""
from tastypie.resources import ModelResource
# from core_app.models import Comment
from tastypie.authorization import Authorization
# from tastypie.authentication import SessionAuthentication
from tastypie import fields
from core_app import utils
# from provider.oauth2.forms import AuthorizationForm
import json
from django.http import HttpResponse

from core_app.models import Comment, myUser
from core_app.auth import SessionBasicAuthentication
from core_app import utils
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


# Mr.German I tried many times to use some libraries for Google authorization
# And nothing works. Some libraries doesn't work with Django 1.7 or another
# strange error
# And now I'll realize own registration.

def login(request):
    # print request.POST
    list_str = str(request.POST.get("list"))
    print list_str
    data = {}
    if request.GET.get('email') and request.GET.get('password'):
        email = request.GET['email']
        password = request.GET['password']

        try:
            user = myUser.objects.get(email=email)
            print user
            print user.password == password
            if user.password == password:
                request.session['id'] = user.pk
                print request.session.get('id')
                return True
        except:
            pass
        return False
    data['form'] = 'You have successfully logined!'
    response_data = json.dumps(data)
    print json.dumps(data)
    return HttpResponse(response_data, content_type='application/json')


class myUserRegistration(ModelResource):
    name = fields.CharField(attribute="name")
    email = fields.CharField(attribute="email")
    password = fields.CharField(attribute="password")

    class Meta:
        queryset = myUser.objects.all()
        resource_name = 'my_user'
        # excludes = ['password']
        # authentication = SessionAuthentication()
        authorization = Authorization()
        always_return_data = True


class CommentResource(ModelResource):
    # user = fields.ForeignKey(CommentResource, 'user')

    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        filtering = {
            # 'user': ALL_WITH_RELATIONS,
            'site_url': ALL_WITH_RELATIONS
            # 'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }

        def dispatch(self, request_type, request, **kwargs):
            print request.META.get('site_url')
            self._meta.queryset.filter(site_url=request.META.get('site_url'))
            return super(CommentResource, self).dispatch(request_type, request, **kwargs)

    # def hydrate(self, bundle):
    # Don't add student with existed email
    # if bundle.obj.email!=bundle.request.student.email:
    # bundle.data['email'] = bundle.obj.email
    #     if bundle.request.method == 'GET':
    #         print bundle.data
    # bundle.obj.pk = bundle.data['pk']
    #         site_url = bundle.data['site_url']

    #         print "New student was successfully added!"
    #     return bundle
