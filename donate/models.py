from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
from FBxGIT import settings
import os
import shutil

# Create your models here.


class User(models.Model):
    FB_ID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    points = models.IntegerField()

    def __str__(self):
        return self.FB_ID


class Goods(models.Model):

    STATUS = (
        ('U', 'UNSOLD'),
        ('S', 'SOLD'),
    )
    CATEGORIES = (
        ('C', 'Clothes'),
        ('M', 'Makeup and Cosmetics'),
        ('O', 'Others'),
    )
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    donor = models.ForeignKey(User, related_name='goods_donor')
    comsumer = models.ForeignKey(User, related_name='goods_consumer', null=True)
    category = models.CharField(max_length=100,
                                choices=CATEGORIES,
                                default='C')
    status = models.CharField(max_length=100,
                              choices=STATUS,
                              default='U')
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='pictures/%d')

    def save(self):
        if self.id is None:
                super(Goods, self).save()
                self.picture = self.get_path(self.picture)
        super(Goods, self).save()

    def get_path(self, filename):
        save_name = os.path.join('pictures', '%s.jpg' % self.id)
        current_path = os.path.join(settings.MEDIA_ROOT, self.picture)
        new_path = os.path.join(settings.MEDIA_ROOT, save_name)
        if os.path.exists(current_path):
                shutil.move(current_path, new_path)
        return save_name

    def __str__(self):
        return self.name


class Charity(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
