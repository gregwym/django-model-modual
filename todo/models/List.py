from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

class List(models.Model):
	name = models.CharField(max_length=200)
	color = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add=True, default=timezone.now)

	def do_first_thing(self, action):
		print 'List is {} first thing'.format(action)

	def do_second_thing(self, action):
		print 'List is {} second thing'.format(action)

	def do_third_thing(self, action):
		print 'List is {} third thing'.format(action)


@receiver(pre_save, sender=List)
def list_pre_save_hook(sender, instance, **kwargs):
	instance.do_first_thing('pre_save')
	instance.do_second_thing('pre_save')
	instance.do_third_thing('pre_save')


@receiver(post_save, sender=List)
def list_post_save_hook(sender, instance, **kwargs):
	instance.do_first_thing('post_save')
	instance.do_second_thing('post_save')
	instance.do_third_thing('post_save')
