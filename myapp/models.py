from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name


class Yeguliklar(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	nomi = models. CharField(max_length=200, null=True, blank=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	narx = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.nomi

class Aloqa(models.Model):
	ism = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)
	xabar = models.CharField(max_length=300, null=True)

	def __str__(self):
		return self.ism

class Stol_Buyurtma(models.Model):
	ism = models.CharField(max_length=100, null=True)
	tel = models.CharField(max_length=100, null=True)
	sana = models.DateField(auto_now_add=False, null=True)
	vaqt = models.TimeField(auto_now_add=False,null=True)
	soni = models.IntegerField(null=True, blank=True)
	izoh = models.CharField(max_length=300, null=True)

	def __str__(self):
		return self.ism
