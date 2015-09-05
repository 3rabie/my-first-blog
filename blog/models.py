from django.db import models
from django.utils import timezone 

class Post(models.Model):
	Auther = models.ForeignKey('auth.User')
	Title = models.CharField(max_length = 200)
	Text = models.TextField()
	Created_date = models.DateTimeField( default = timezone.now)
	Published_date = models.DateTimeField( blank = True , null = True)

	def publish(self):
		self.Published_date = timezone.now()
		self.save()

def __str__(self):
	return self.Title
