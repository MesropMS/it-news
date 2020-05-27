from django.db import models
from  django_extensions.db.fields import RandomCharField
from cloudinary.models import CloudinaryField
# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=300)
	slug = RandomCharField(length=8)

	def __str__(self):
		return self.name

class Post(models.Model):
	group = models.ManyToManyField(Group)
	title = models.CharField(max_length=300)
	text = models.TextField()
	img = CloudinaryField('video')
	slug = RandomCharField(length=5)
	date = models.DateTimeField(auto_now_add=True)
	view = models.IntegerField(default=0)
	def __str__(self):
		return self.title