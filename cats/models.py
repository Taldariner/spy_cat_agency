from django.db import models
from .validators import validate_breed


class SpyCat(models.Model):
	name = models.CharField(max_length = 128)
	years_of_expirience = models.IntegerField(default = 0)
	breed = models.CharField(max_length = 128, validators = [validate_breed])
	salary = models.IntegerField(default = 0)
