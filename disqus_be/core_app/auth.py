from core_app.models import myUser
from tastypie.authentication import BasicAuthentication

class SessionBasicAuthentication(BasicAuthentication):
    '''
     If the user is already authenticated by a django session it will 
     allow the request (useful for ajax calls) . If it is not, defaults
     to basic authentication, which other clients could use.
    '''
    def __init__(self, *args, **kwargs):
        super(SessionBasicAuthentication, self).__init__(*args, **kwargs)

    def is_authenticated(self, request, **kwargs):
        print kwargs
        # auth_info = request.META.get('HTTP_AUTHORIZATION')
        # pritn auth_info
        print request
        # if request.GET.get('email') and request.GET.get('password'):
        #     email = request.GET['email']
        #     password = request.GET['password']
        #     print email
        #     print password
        #     try:
        #         user = myUser.objects.get(email = email)
        #         print user
        #         print user.password == password
        #         if user.password == password:
        #             request.session['id'] = user.pk
        #             print request.session.get('id')
        #             return True
        #     except:
        #         pass
        #     return False
        # from django.contrib.sessions.models import Session
        # if 'sessionid' in request.COOKIES:
        #     s = Session.objects.get(pk=request.COOKIES['sessionid'])
        #     if '_auth_user_id' in s.get_decoded():
        #         user = myUser.objects.get(pk=s.get_decoded()['_auth_user_id'])
        #         request.user = user
        #         print request
        #         print 'logined'
        #         return True
        return True
        return super(SessionBasicAuthentication, self).is_authenticated(request, **kwargs)