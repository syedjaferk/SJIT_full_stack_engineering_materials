from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from orders.models import Order


@receiver(post_save, sender=Order)
def send_notifications(sender, instance, created, **kwargs):
	print("Inside Notifications")
	if created:
		print("An Order has been created")
