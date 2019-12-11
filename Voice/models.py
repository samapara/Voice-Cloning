from django.db import models


# Create your models here.

class InputText(models.Model):
    inputText = models.CharField(max_length=50)
