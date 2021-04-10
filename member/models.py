from django.db import models
from django.forms import CharField


class Member(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True)
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    current_residence = models.CharField(max_length=100,default='')
    preferred_residence = models.CharField(max_length=100,default='')
    admin_whether = models.CharField(max_length=1,default='N')
# Create your models here.
