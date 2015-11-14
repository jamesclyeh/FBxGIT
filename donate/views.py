from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from donate.models import Goods

# Create your views here.

def index(request):
    return TemplateResponse(request, 'index.html', {})

def fonts(request):
    return redirect('/static/%s'%request.path)

def full_list(request, category=None):
    dic = {}
    dic['category'] = category
    if not category: dic['goods'] = Goods.objects.all()
    else: dic['goods'] = Goods.objects.all().filter(category=category) 
    for goods in dic['goods']:
        goods.picture = '/'.join(str(goods.picture).split('/')[1:])
    return TemplateResponse(request, 'full_list.html', dic)

def add_list(request):
    dic = {}
    dic['cats'] = enumerate(set(x.category for x in Goods.objects.all()));
    return TemplateResponse(request, 'add_list.html', dic)

def getUser(request):
    dic = {}
    u = User.objects.get(FB_ID = request.GET['FB_ID'])
    lis = u.goods_donor.all()
    dic['user'] = u
    dic['goods'] = lis
    return TemplateResponse(request, 'profile.html', dic)

@csrf_exempt
def upload(request):
    formset = GoodsForm(request.POST)
    if formset.is_valid():
        print "HERE"
        g = Goods(
            price = request.POST.get('price', ''),
            description = request.POST.get('description', ''),
            donor = request.COOKIES['user_id'],
            category = request.POST.get('category', ''),
            picture = request.POST.get('picture', '')
        )
        g.save()
    print "NOW"
    return HttpResponse("Text", context_type = 'text/plain')

@csrf_exempt
def sold(request):
    formset = GoodsForm(request.POST)
    if formset.is_valid():
        print "HERE"
        Goods.objects.filter(pk=request.POST.get('pk', '')).update(consumer=request.POST.get('consumer', ''))
        Goods.objects.filter(pk=request.POST.get('pk', '')).update(status='S')
    print "NOW"
    return HttpResponse("Text", context_type = 'text/plain')

def fblogin(request):
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'latest_question_list': '123',
    })
    return HttpResponse(template.render(context))
