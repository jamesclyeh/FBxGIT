from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from donate.models import Goods

# Create your views here.

def index(request):
    return TemplateResponse(request, 'index.html', {})

def fonts(request):
    return redirect('/static/%s'%request.path)

def full_list(request):
    dic = {}
    dic['goods'] = Goods.objects.all()
    for goods in dic['goods']:
        goods.picture = '/'.join(str(goods.picture).split('/')[1:])
    return TemplateResponse(request, 'full_list.html', dic)

def add_list(request):
    dic = {}
    return TemplateResponse(request, 'add_list.html', dic)

def upload(request):
    formset = GoodsForm(request.POST)
    if formset.is_valid():
        print "HERE"
        g = Goods(
            price = request.POST.get('price', ''),
            description = request.POST.get('description', ''),
            donor = request.COOKIES['id'],
            category = request.POST.get('category', ''),
            picture = request.POST.get('picture', '')
        )
        g.save()
    print "NOW"
    return HttpResponse("Text", context_type = 'text/plain')

def fblogin(request):
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'latest_question_list': '123',
    })
    return HttpResponse(template.render(context))
