from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply_loan, name='apply_loan'),
    path('status/', views.check_status, name='check_status'),
]
