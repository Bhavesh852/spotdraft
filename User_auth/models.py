from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PDF_Detail(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	pdf_title = models.CharField(max_length=30)
	pdf_description = models.CharField(max_length=200)
	pdf = models.FileField(upload_to='user_auth/document')

	def __str__(self):
		return self.pdf_title

class Comment(models.Model):
	pdf_for = models.ForeignKey(PDF_Detail, on_delete=models.CASCADE)
	by_user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.CharField(max_length=200)