from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display/', views.display_data, name='display'),
     path('form/', views.user_data, name='user_data'),
    path('success/', views.success, name='success'),
]