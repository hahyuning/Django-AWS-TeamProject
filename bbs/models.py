from django.db import models

# Create your models here.
class Bbs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    writer = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']