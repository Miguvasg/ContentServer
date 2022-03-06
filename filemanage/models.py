from django.db import models

# Create your models here.

class Files(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    size = models.CharField(max_length=50, blank=False, null=False)
    docfile = models.FileField()
