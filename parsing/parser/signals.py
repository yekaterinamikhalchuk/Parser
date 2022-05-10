from django.conf import settings
from .tasks import hackernews_rss
from .models import Url
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Url, *args, **kwargs)
def notify_subscribers(sender, instance):
    print(kwargs)
    print(instance)
    url_instance = instance.link

    # print(url_instance)
    # hackernews_rss.delay(url_instance)
