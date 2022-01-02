from django.db.models.signals import pre_save, post_save
from .models import Order,Payment
from django.dispatch import receiver
import random
import string

sr = random.SystemRandom()

@receiver(pre_save, sender=Order)
def refrence_code_genarator(sender, instance, *agrs, **kwargs):
	ch = sr.choices(string.digits, k=8)
	ch += sr.choices(string.ascii_letters, k=4)
	sr.shuffle(ch)
	ch = ''.join(ch)
 
	try:
		instance.refrence_code = ch
	except:
		sr.shuffle(ch)
		ch = ''.join(ch)
		instance.refrence_code = ch