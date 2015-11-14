from django.db import models

# Create your models here.


class Goods(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField(min_value=0)
    description = models.TextField(max_length=300)
    picture = models.ImageField(upload_to='photos/%d' % self.id)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return name


class Charity(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
