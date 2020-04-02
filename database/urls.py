from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('fill', views.fill, name='fill')
]
