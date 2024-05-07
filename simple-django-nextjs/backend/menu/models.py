from django.db import models
from datetime import * 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(1000000)])