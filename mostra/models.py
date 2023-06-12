from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Artista(models.Model):
	nome = models.CharField(max_length=250)
	biografia = models.TextField()
	data = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ["-data"]

	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		return reverse("artista_detail", kwargs={"pk": self.pk})

class Opera(models.Model):
	titolo = models.CharField(max_length=250)
	artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name="artista")
	descrizione = models.TextField()
	data = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ["-data"]
	def __str__(self):
		return self.titolo

	def get_absolute_url(self):
		return reverse("opera_detail", kwargs={"pk": self.pk})

class Collezione(models.Model):
	nominativo = models.CharField(max_length=250)
	info = models.TextField()
	#opera = models.ManyToManyField('Opera', blank=True, related_name='collezione')
	opera = models.ManyToManyField(Opera, related_name="opera")
	data = models.DateTimeField(auto_now=False, auto_now_add=True)
	proprietario = models.CharField(max_length=250)

	class Meta:
		ordering = ["-data"]
	
	
	def __str__(self):
		return self.nominativo
	
	def get_absolute_url(self):
		return reverse("collezione_detail", kwargs={"pk": self.pk})



		
class Modifiche(models.Model):
	#name = models.EmailField('Venue Name'),
	#adress = models.URLField(max_length=250),
	#zip_code = models.CharField('Zip Code', max_length=250),
	#phone = models.CharField('Contact Phone', max_length=250),
	#web = models.URLField('Website Adress')
	
	name = models.CharField('Nome', max_length=250)
	email_adress = models.EmailField('Email')
	text = models.TextField('Modifiche che vuoi inviarci')

	def __str__(self):
		return self.name

