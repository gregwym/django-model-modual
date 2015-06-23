from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	list = models.ForeignKey('todo.List', related_name='items')
	created = models.DateTimeField(auto_now_add=True, default=timezone.now)
	completed = models.DateTimeField(null=True)

	def do_first_thing(self, action):
		print 'Item is {} first thing'.format(action)

	def do_second_thing(self, action):
		print 'Item is {} second thing'.format(action)

	def do_third_thing(self, action):
		print 'Item is {} third thing'.format(action)


@receiver(pre_save, sender=Item)
def item_pre_save_hook(sender, instance, **kwargs):
	instance.do_first_thing('pre_save')
	instance.do_second_thing('pre_save')
	instance.do_third_thing('pre_save')


@receiver(post_save, sender=Item)
def item_post_save_hook(sender, instance, **kwargs):
	instance.do_first_thing('post_save')
	instance.do_second_thing('post_save')
	instance.do_third_thing('post_save')
