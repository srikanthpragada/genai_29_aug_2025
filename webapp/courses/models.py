from django.db import models

class Course(models.Model):
	title = models.CharField(max_length=100)
	duration = models.CharField(max_length=50)
	fee = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.title
