from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("add/", views.add_suivi_tnt, name="add-suivi-tnt"),
    path('import/', views.import_data, name="import-data"),

]
