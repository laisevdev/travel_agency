from django import forms
from .models import Clients_Register, Trip_Agenda

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Clients_Register
        fields = ('name', 'cpf', 'rg',)

        
class AgendaForm(forms.ModelForm):

    class Meta:
        model = Trip_Agenda
        fields = ('travel_date', 'trip_destination', 'transferred', 'payment_methods', 'id_client',)
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }

     
       
        