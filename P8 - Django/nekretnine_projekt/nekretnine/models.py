from django.db import models


class Nekretnina(models.Model):
	ime = models.CharField(verbose_name="Ime", max_length=250, blank=True)
	sifra = models.PositiveIntegerField(verbose_name="Šifra", null=True)
	ukupna_povrsina = models.PositiveIntegerField(verbose_name="Ukupna površina [m2]", null=True)
	godina_izgradnje_objekta = models.PositiveIntegerField(null=True)
	adresa = models.CharField(max_length=250, blank=True)
	post_broj = models.PositiveIntegerField(verbose_name="Poštanski broj", null=True)
	ostalo = models.CharField(max_length=250, blank=True)

	class Meta:
		app_label = 'nekretnine'
		verbose_name = 'Nekretnina'
		verbose_name_plural = 'Nekretnine'
	
	def __str__(self):
		return str(self.id)

