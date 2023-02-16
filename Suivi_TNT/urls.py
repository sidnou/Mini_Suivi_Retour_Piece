from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("suivi-tnt/add/", views.add_suivi_tnt, name="add-suivi-tnt"),

]
