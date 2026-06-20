from django.contrib import admin

#from django.contrib import admin
from .models import Entreprise, Salon, Employe, Client, Prestation, Reservation, Paiement, Notification



class SalonAdmin(admin.ModelAdmin):
    list_display = ('nom_salon', 'num_telephone', 'email', 'nom_gerant')# liste les champs que nous voulons sur l'affichage de la liste
# Enregistrement de tous vos modèles
admin.site.register(Entreprise)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Employe)
admin.site.register(Client)
admin.site.register(Prestation)
admin.site.register(Reservation)
admin.site.register(Paiement)
admin.site.register(Notification)

