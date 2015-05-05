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

# def get_form(request):
#     data = {}
#     data['title'] = 'Course registration'
#     form = {}
#     form['name'] = 'Name'
#     form['surname'] = 'Surname'
#     form['email'] = 'example@mail.com'
#     form['phone'] = '+7(777)777-77-77'
#     form['lessons_time'] = ['morning', 'afternoon', 'evening']
#     form['program_preferences'] = [
#         'Foundation', 'IELTS', 'TOEFL', 'SAT', 'another']
#     data['form'] = form
#     response_data = json.dumps(data)
#     print json.dumps(data)
#     return HttpResponse(response_data, content_type='application/json')

def login(request):
    # print request.POST
    list_str = str(request.POST.get("list"))
    print list_str
    data={}
    if request.GET.get('email') and request.GET.get('password'):
        email = request.GET['email']
        password = request.GET['password']

        try:
            user = myUser.objects.get(email = email)
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


# class myUserAuthentication(ModelResource):
#     name = fields.CharField(attribute="name")
#     email = fields.CharField(attribute="email")
#     password = fields.CharField(attribute="password")

#     class Meta:
#         queryset = myUser.objects.all()
#         resource_name = 'sign_in'
#         excludes = ['name']
# filtering = {"status": ALL }
# filtering = {
# "email": ALL_WITH_RELATIONS,
# "password": ALL_WITH_RELATIONS
# }
#         authorization = Authorization()
# authentication = SessionBasicAuthentication()
#         always_return_data = True

#     def hydrate(self, bundle):
#         print bundle
#         if self.is_authenticated(bundle.request):
#             pass
#         else:
#             print bundle.data
#             if bundle.data.get('email') and bundle.data.get('password'):
#                 email = bundle.data['email']
#                 password = bundle.data['password']
#                 try:
#                     user = myUser.objects.get(email=email)
#                     if user.password == password:
#                         bundle.request.session['user_id'] = user.pk
#                         bundle.data[
#                             'message'] = 'You have successfully signed in!'
#                         print bundle.request.session.get('user_id')
#                 except:
#                     bundle.data['error'] = 'User with such email is not exist'
# print bundle.request
#         return bundle

    # def hydrate(self, bundle):
    #     if bundle.request.method == 'POST':
    #         print bundle.data
    # bundle.obj.pk = bundle.data['pk']
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
        # authorization = Authorization()
        filtering = {
            # 'user': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
