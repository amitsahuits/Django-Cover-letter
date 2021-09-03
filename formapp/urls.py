
from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.formfunction),
    path('Resume/',views.resumemakerfunction)
]
