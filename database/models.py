from django.db import models

class Pulsar(models.Model):
    Name = models.CharField(max_length=200, help_text="Pulsar name.  The B name if exists, otherwise the J name.")
