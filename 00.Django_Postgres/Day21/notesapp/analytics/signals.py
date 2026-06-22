from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from orders.models import Order


@receiver(post_save, sender=Order)
def log_event(sender, instance, created, **kwargs):
	if created:
		print("Analytics logged")
