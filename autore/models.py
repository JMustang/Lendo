from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=255)