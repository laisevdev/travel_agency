from django.db import models
from django.utils import timezone

class Clients_Register(models.Model):
    name = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=12, unique=True)
    creation_date = models.DateTimeField(auto_now = False, auto_now_add = False, default=timezone.now())

    def __str__(self):
        return self.name

class Trip_Agenda(models.Model):
    trip_destination =  models.CharField(max_length=100)
    transferred =  models.CharField(max_length=100)
    travel_date = models.DateTimeField(auto_now = False, auto_now_add = False, null=True, blank=True)
    PAYMENTS_CHOICES = [
        ('pix', 'PIX'),
        ('boleto', 'BOLETO'),
        ('transferencia_bancaria', 'TRANSFERÊNCIA BANCÁRIA'),
        ('cartao_de_credito', 'CARTÃO DE CRÉDITO'),
        ('cartao_de_debito', 'CARTÃO DE DÉBITO'),  
        ('bitcoin_ou_criptomoedas', 'BITCOIN OU CRIPTOMOEDAS'),        
    ]
    payment_methods = models.CharField(max_length=30, choices=PAYMENTS_CHOICES)
    creation_date = models.DateTimeField(auto_now = False, auto_now_add = False, default=timezone.now())
    id_client = models.ForeignKey(Clients_Register, on_delete=models.CASCADE)

    def created_at(self):
        self.creation_date = timezone.now()
        self.save()
        return self.id_client