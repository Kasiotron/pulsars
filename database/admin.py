from django.contrib import admin

from .models import Pulsar, Observation
admin.site.register(Pulsar)
admin.site.register(Observation)
