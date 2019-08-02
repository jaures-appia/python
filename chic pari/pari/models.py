from django.db import models

class Client(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=100)
	email = models.EmailField()
	telephone = models.CharField(max_length=11)
	mdp = models.CharField(max_length=100)
	date_inscription = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return "{} {}".format(self.nom, self.prenom)


# Create your models here.
