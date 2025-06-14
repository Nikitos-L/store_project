from django.db.models.signals import post_save
from django.dispatch import receiver

from bot_tg import notification_for_user
from products.models import Orders


@receiver(post_save, sender=Orders)
def create_notification_tg_bot(sender, instance, created, **kwargs):
    if created:
        username = instance.user
        notification_for_user(str(username))