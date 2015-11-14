from django.conf.urls import include, url
from django.contrib import admin

from donate import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.fblogin, name='fblogin'),
    url(r'^full_list/$', views.full_list, name='full_list'),
    url(r'^full_list/(?P<category>.+)/$', views.full_list, name='full_list'),
    url(r'^add_list/', views.add_list, name='add_list'),
    url(r'^check_out/', views.check_out, name='check_out'),
    url(r'^upload', views.upload, name='upload'),
    url(r'^fonts/.*', views.fonts, name='fonts'),
    url(r'^facebook_connect/', include('facebook_connect.urls')),
]
