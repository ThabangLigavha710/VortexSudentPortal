from django.db import models

# Create your models here.
class Search(models.Model):
	search = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.search)

	class Meta:
		verbose_name_plural = 'Searches'

class create_user(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email_address = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=10)
	gender = models.CharField(max_length=6)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length= 20)
	course = models.CharField(max_length= 60)
	current_year = models.CharField(max_length=15)