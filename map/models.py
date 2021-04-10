from django.db import models

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    classification = models.CharField(max_length=100)
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    gu = models.CharField(max_length=100, default="")
    agency = models.CharField(max_length=100, default="")
    user = models.CharField(max_length=100, default="")
    cost = models.CharField(max_length=100, default="")
    casting = models.CharField(max_length=100, default="")
    information = models.TextField(default="")
    etc = models.TextField(default="")
    url = models.URLField("site url")
    img = models.ImageField(upload_to='photos', default='photos/no_image.png')
    start_date = models.CharField(max_length=100, default="")
    end_date = models.CharField(max_length=100, default="")
    tel = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")

