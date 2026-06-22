from django.db import models

# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Publisher(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name 

class Book(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField()
	author = models.ForeignKey(
			Author,
			on_delete=models.CASCADE,
			related_name="books"
		)
	publisher = models.ForeignKey(
			Publisher,
			on_delete=models.CASCADE,
			related_name="books"
		)

	def __str__(self):
		return self.title