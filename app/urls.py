from django.urls import path
from app import views

urlpatterns =[
    # inicio
    path('', views.inicio, name="inicio"),
]