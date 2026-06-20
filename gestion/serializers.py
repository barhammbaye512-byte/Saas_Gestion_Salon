from rest_framework import serializers
from .models import Entreprise, Salon, Employe, Client, Prestation, Reservation, Paiement, Notification

class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class PrestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    client_nom = serializers.SerializerMethodField()
    employe_nom = serializers.SerializerMethodField()
    prestation_nom = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = '__all__'

    def get_client_nom(self, obj):
        return f'{obj.client.prenom_client} {obj.client.nom_client}' if obj.client else ''

    def get_employe_nom(self, obj):
        return f'{obj.employe.prenom_employe} {obj.employe.nom_employe}' if obj.employe else ''

    def get_prestation_nom(self, obj):
        return obj.prestation.nom_prestation if obj.prestation else ''

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'