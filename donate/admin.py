from django.contrib import admin
from donate.models import Goods, Charity, User

# Register your models here.
admin.site.register(Goods)
admin.site.register(Charity)
admin.site.register(User)
