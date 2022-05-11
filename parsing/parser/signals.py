from django.conf import settings
from .tasks import hackernews_rss
from .models import Url
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import JsonResponse

@receiver(pre_save, sender=Url)
def notify_subscribers(sender, instance, **kwargs):

    url_instance = instance.link
    url_id = instance.id
    hackernews_rss.delay(url_instance, instance)