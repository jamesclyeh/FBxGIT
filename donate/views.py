from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


from donate.models import Charity
from donate.models import Goods
from donate.models import User
from donate.form import GoodsForm

from facebook_connect.facebook_python_sdk import facebook

import urllib

# Create your views here.
def index(request):
    dic = {}
    # u = User.objects.get(FB_ID = request.GET['FB_ID'])
    # lis = u.goods_donor.all()
    # dic['user'] = u
    # dic['goods'] = lis
    if 'fb_token' in request.COOKIES:
      token = request.COOKIES['fb_token']
      pic = urllib.urlopen("https://graph.facebook.com/me/picture?"+urllib.urlencode({'access_token':token, 'height':200})).read()

    return TemplateResponse(request, 'index.html', {})

def fonts(request):
    return redirect('/static/%s'%request.path)

def check_out(request):
    return TemplateResponse(request, 'check_out.html', {})

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
    dic['cats'] = set(x.category for x in Goods.objects.all());
    dic['charity'] = set(x.name for x in Charity.objects.all());
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
    u = User.objects.get(FB_ID = request.COOKIES['user_id'])
    c = Charity.objects.get(name = request.POST['charity'])
    g = Goods(
        name = request.POST.get('name', ''),
        price = request.POST.get('price', ''),
        description = request.POST.get('description', ''),
        donor = u,
        charity_donor = c,
        category = request.POST.get('category', ''),
        picture = request.POST.get('picture', ''),
        charity_consumer = c,
    )
    g.save()

    # print facebook.GraphAPI(request.COOKIES['fb_token']).put_wall_post(
    #     "I just put this item up to raise money for charity!!",
    #     {"name": "Charty exchange",
    #      "link": "http://140.113.89.232:12345/full_list/",
    #      "caption": request.POST.get('name', ''),
    #      "description": request.POST.get('description', '')})

    return TemplateResponse(request, 'index.html', {})

@csrf_exempt
def sold(request):
    g = Goods.objects.filter(pk=request.POST.get('pk', ''))
    g.update(status='S')
    return TemplateResponse(request, 'index.html', {})

def fblogin(request):
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'latest_question_list': '123',
    })
    return HttpResponse(template.render(context))
