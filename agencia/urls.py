from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.client_register, name='client_register'),
    path('sucessfullregister/', views.register_sucess, name='sucessfull_register'),
    path('travelregister/', views.travel_register, name='travel_register'),
    path('sucessbook/', views.sucessfull_booking, name='sucessfull_booking'),
    path('showclients/', views.search, name='search'),
    path('showdestinations/', views.travel_search, name='travel_search'),
]