from django.db import models

class Entreprise(models.Model):
    nom_entreprise = models.CharField(max_length=200)
    type_abonnement = models.CharField(max_length=100)

    class Meta:
        db_table = 'Entreprise'

    def __str__(self):
        return self.nom_entreprise


class Salon(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom_salon = models.CharField(max_length=200)
    adresse_salon = models.CharField(max_length=300)
    num_telephone = models.CharField(max_length=20)
    email = models.EmailField()
    date_creation = models.DateField()
    nom_gerant = models.CharField(max_length=100)
    horaire_ouverture = models.TimeField()

    class Meta:
        db_table = 'Salon'

    def __str__(self):
        return self.nom_salon


class Employe(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    nom_employe = models.CharField(max_length=100)
    prenom_employe = models.CharField(max_length=100)
    num_tel_employe = models.CharField(max_length=20)
    specialisation = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    date_embauche = models.DateField()
    grade = models.CharField(max_length=50)

    class Meta:
        db_table = 'Employe'

    def __str__(self):
        return f'{self.prenom_employe} {self.nom_employe}'


class Client(models.Model):
    nom_client = models.CharField(max_length=100)
    prenom_client = models.CharField(max_length=100)
    num_tel_client = models.CharField(max_length=20)
    email_client = models.EmailField(unique=True)
    date_inscription = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Client'

    def __str__(self):
        return f'{self.prenom_client} {self.nom_client}'


class Prestation(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    employes = models.ManyToManyField(Employe, blank=True)
    nom_prestation = models.CharField(max_length=200)
    duree_prestation = models.IntegerField(help_text="Durée en minutes")
    prix = models.FloatField()
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'Prestation'

    def __str__(self):
        return self.nom_prestation


class Reservation(models.Model):
    STATUTS = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
        ('terminee', 'Terminée'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.SET_NULL, null=True)
    prestation = models.ForeignKey(Prestation, on_delete=models.SET_NULL, null=True)
    date_reserver = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField() 
    avis = models.TextField(blank=True)
    statut = models.CharField(max_length=20, choices=STATUTS, default='en_attente')

    class Meta:
        db_table = 'Reservation'

    def __str__(self):
        return f'Réservation {self.id} - {self.client}'


class Paiement(models.Model):
    METHODES = [
        ('carte', 'Carte bancaire'),
        ('especes', 'Espèces'),
        ('mobile', 'Mobile Money'),
    ]
    STATUTS = [
        ('en_attente', 'En attente'),
        ('paye', 'Payé'),
        ('rembourse', 'Remboursé'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    montant = models.FloatField()
    methode_de_paiement = models.CharField(max_length=20, choices=METHODES)
    date_de_paiement = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUTS, default='en_attente')

    class Meta:
        db_table = 'Paiement'

    def __str__(self):
        return f'Paiement {self.id} - {self.montant} FCFA'


class Notification(models.Model):
    TYPES = [
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('push', 'Notification Push'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type_notification = models.CharField(max_length=20, choices=TYPES)
    message = models.TextField()
    date_envoie = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Notification'

    def __str__(self):
        return f'Notification {self.type_notification} - {self.client}'
