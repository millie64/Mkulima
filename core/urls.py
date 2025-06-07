from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-farmer/', views.add_farmer, name='add_farmer'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-order/', views.add_order, name='add_order'),
    path('add-report/', views.add_report, name='add_report'),
    path('add-vet/', views.add_vet, name='add_vet'),
    path('add-consultation/', views.add_consultation, name='add_consultation'),
    path('add-ai/', views.add_ai, name='add_ai'),
    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('dashboard/', views.dashboard, name='dashboard'),


]
