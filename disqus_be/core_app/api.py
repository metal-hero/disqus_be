"""This module contains API resource classes"""
from tastypie.resources import ModelResource
# from core_app.models import Comment
from tastypie.authorization import Authorization
from tastypie import fields
from core_app import utils
# from provider.oauth2.forms import AuthorizationForm
import json
from django.http import HttpResponse

from core_app.models import Comment
from core_app import utils
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


def login(request):
    # authorization_form = AuthorizationForm()
    # g = authorization_form.save()
    # print q
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


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
