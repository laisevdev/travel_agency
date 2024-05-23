from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.client_register, name='client_register'),
    path('sucessfullregister/', views.register_sucess, name='sucessfull_register'),
]