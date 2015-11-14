from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.template.response import TemplateResponse

from donate.models import Goods

# Create your views here.

def index(request):
    return TemplateResponse(request, 'index.html', {})

def full_list(request):
    dic = {}
    dic['goods'] = Goods.objects.all()
    return TemplateResponse(request, 'full_list.html', dic)

def add_list(request):
    dic = {}
    return TemplateResponse(request, 'add_list.html', dic)

def upload(request):
    g = Goods(name = request.POST.get('name', ''),
        price = request.POST.get('price', ''),
        description = request.POST.get('description', ''),
        donor = request.POST.get('donor', ''),
        comsumer = request.POST.get('comsumer', ''),
        category = request.POST.get('category', ''),
        status = request.POST.get('status', ''),
        created_at = request.POST.get('created_at', ''),
        picture = request.POST.get('picture', '')
    )
    g.save()
    return HttpResponse(simplejson.dumps({'success':False}),mimetype = 'application/json')

def fblogin(request):
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'latest_question_list': '123',
    })
    return HttpResponse(template.render(context))
