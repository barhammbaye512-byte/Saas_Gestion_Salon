
from django.contrib import admin
from django.urls import path
from gestion import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter                  
from gestion.views import (
    ClientViewSet,
    EmployeViewSet,
    EntrepriseViewSet,
    NotificationViewSet,
    PaiementViewSet,
    PrestationViewSet,
    ReservationViewSet,
    SalonViewSet,
)

# 1. On configure le routeur automatique pour les clients
router = DefaultRouter()
# 2. On enregistre TOUTES les tables une par une
router.register(r'entreprises', EntrepriseViewSet, basename='entreprise')
router.register(r'salons', SalonViewSet, basename='salon')
router.register(r'employes', EmployeViewSet, basename='employe')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'prestations', PrestationViewSet, basename='prestation')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'paiements', PaiementViewSet, basename='paiement')
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('api/',include(router.urls)),
]
