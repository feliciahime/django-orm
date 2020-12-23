from django.db import models

# Create your models here.
class NewCatPost(models.Model):
    catname = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=120)
    text = models.TextField()
    image = models.URLField(max_length=120)
    sighted = models.DateTimeField()
