from django.db import models

# Create your models here.

class Files(models.Model):
    name = models.CharField(max_length=50)
    docfile = models.FileField()
