from django.db import models



class News(models.Model):
    domain = models.CharField(max_length=200)
    link = models.CharField(max_length=2083, default="")
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    country = models.CharField(max_length=200)
    is_dead = models.BooleanField()
    a = models.CharField(max_length=200)
    ns = models.CharField(max_length=200)
    cname = models.CharField(max_length=200)
    mx = models.CharField(max_length=200)
    txt = models.CharField(max_length=200)