from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.form_manual, name="form_manual")
]