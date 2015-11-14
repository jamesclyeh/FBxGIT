from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.template.response import TemplateResponse

# Create your views here.

def index(request):
    return TemplateResponse(request, 'index.html', {})

def full_list(request):
    return TemplateResponse(request, 'full_list.html', {})

def fblogin(request):
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'latest_question_list': '123',
    })
    return HttpResponse(template.render(context))
