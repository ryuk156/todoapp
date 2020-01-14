from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    
]