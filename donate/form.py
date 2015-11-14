from django.forms import ModelForm
from .models import Goods


class GoodsForm(ModelForm):

    class Meta:
        model = Goods
        fields = ['name', 'price', 'description', 'category', 'picture']
