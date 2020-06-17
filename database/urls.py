from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('view_all', views.view_all, name='view_all'),
    path('fill', views.fill, name="fill"),
    path('fill2', views.fill2, name="fill2")
]
