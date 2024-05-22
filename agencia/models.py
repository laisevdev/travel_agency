from django.db import models
from django.utils import timezone

class Clients_Register(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=10, unique=True)
    creation_date = models.DateTimeField(auto_now = False, auto_now_add = False, default=timezone.now())

    def __str__(self):
        return self.nome

class Trip_Agenda(models.Model):
    trip_destination =  models.CharField(max_length=100)
    transferred =  models.CharField(max_length=100)
    travel_date = models.DateTimeField(auto_now = False, auto_now_add = False, null=True, blank=True)
    PAYMENTS_CHOICES = [
        ('PIX', 'PIX'),
        ('BOLETO', 'BOLETO'),
        ('TRANSFERÊNCIA BANCÁRIA', 'TRANSFERÊNCIA BANCÁRIA'),
        ('CARTÃO DE CRÉDITO', 'CARTÃO DE CRÉDITO'),
        ('CARTÃO DE DÉBITO', 'CARTÃO DE DÉBITO'),  
        ('BITCOIN OU CRIPTOMOEDAS', 'BITCOIN OU CRIPTOMOEDAS'),        
    ]
    payment_methods = models.CharField(max_length=30, choices=PAYMENTS_CHOICES)
    creation_date = models.DateTimeField(auto_now = False, auto_now_add = False, default=timezone.now())
    id_paciente = models.ForeignKey(Clients_Register, on_delete=models.CASCADE)

    def created_at(self):
        self.creation_date = timezone.now()
        self.save()
        return self.id_paciente