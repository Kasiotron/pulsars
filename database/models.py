from django.db import models

class Pulsar(models.Model):
    Name = models.CharField(max_length=200)
