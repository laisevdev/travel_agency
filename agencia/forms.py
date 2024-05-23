from django import forms
from .models import Clients_Register, Trip_Agenda

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Clients_Register
        fields = ('name', 'cpf', 'rg',)

        
class AgendaForm(forms.ModelForm):

    class Meta:
        model = Trip_Agenda
        fields = ('id_paciente', 'trip_destination', 'transferred', 'payment_methods',)
        widgets = {
            'travel_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        