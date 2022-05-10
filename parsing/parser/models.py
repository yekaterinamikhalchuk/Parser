from django.db import models



class News(models.Model):
    domain = models.CharField(max_length=200)
    link = models.ForeignKey(Url, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    country = models.CharField(max_length=200, null=True)
    is_dead = models.BooleanField()
    a = models.CharField(max_length=200, null=True)
    ns = models.CharField(max_length=200, null=True)
    cname = models.CharField(max_length=200, null=True)
    mx = models.CharField(max_length=200, null=True)
    txt = models.CharField(max_length=200, null=True)


class Url(models.Model):
    link = models.URLField(
        _("Trip Number"),
        max_length=128,
        blank=True
    )