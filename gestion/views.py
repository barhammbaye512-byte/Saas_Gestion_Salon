from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')
from django.http import JsonResponse

from .models import Client
from .serializers import ClientSerializer

# Cette classe gère automatiquement tout le CRUD des clients
from rest_framework import viewsets
from .models import Entreprise, Salon, Employe, Client, Prestation, Reservation, Paiement, Notification
from .serializers import (
    EntrepriseSerializer, SalonSerializer, EmployeSerializer, 
    ClientSerializer, PrestationSerializer, ReservationSerializer, 
    PaiementSerializer, NotificationSerializer
)

# 1. Le CRUD pour les Entreprises
class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer

# 2. Le CRUD pour les Salons
class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

# 3. Le CRUD pour les Employés
class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

# 4. Le CRUD pour les Clients
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# 5. Le CRUD pour les Prestations
class PrestationViewSet(viewsets.ModelViewSet):
    queryset = Prestation.objects.all()
    serializer_class = PrestationSerializer

# 6. Le CRUD pour les Réservations
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# 7. Le CRUD pour les Paiements
class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

# 8. Le CRUD pour les Notifications
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date, time
# Importation de vos vrais modèles Django
from .models import Entreprise, Salon 

@api_view(['POST'])
def register_salon(request):
    try:
        # 1. On récupère les données envoyées par votre fichier Angular
        data = request.data
        
        # 2. Sécurité : On vérifie si un salon utilise déjà cet email
        if Salon.objects.filter(email=data.get('email')).exists():
            return Response(
                {"message": "Un salon possède déjà cette adresse email."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 3. Création automatique de l'Entreprise (gère l'abonnement du SaaS)
        nouvelle_entreprise = Entreprise.objects.create(
            nom_entreprise=data.get('nom'), # Reçoit nomSalon d'Angular
            type_abonnement=data.get('offre_choisie') # Reçoit l'offre
        )
        
        # 4. Création du Salon relié à cette entreprise avec vos vrais champs
        nouveau_salon = Salon.objects.create(
            entreprise=nouvelle_entreprise,
            nom_salon=data.get('nom'),
            adresse_salon=data.get('adresse'),
            num_telephone=data.get('telephone'),
            email=data.get('email'),
            nom_gerant=data.get('gerant'),
            
            # Vos champs obligatoires en BDD initialisés proprement pour le démarrage :
            date_creation=date.today(), # Date du jour automatique
            horaire_ouverture=time(9, 0) # Par défaut 09:00, modifiable sur le dashboard
        )
        
        # En production, n'oubliez pas d'ajouter un champ password à votre modèle Salon 
        # ou d'utiliser le modèle User de Django pour gérer la connexion sécurisée du gérant.

        return Response(
            {
                "message": "Inscription réussie !",
                "salon_id": nouveau_salon.id,
                "entreprise_id": nouvelle_entreprise.id
            }, 
            status=status.HTTP_201_CREATED
        )
        
    except Exception as e:
        return Response(
            {"message": f"Erreur côté serveur : {str(e)}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
