from django.http import HttpResponse, HttpRequest
from django.template import loader
from rest_framework.authtoken.models import Token


def testing(request):
  token="x";
  template = loader.get_template('admin/token/token.html')
  context = {
    'firstname': token
  }
  return HttpResponse(template.render(context, request))
  # Create your views here.
