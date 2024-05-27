from django.shortcuts import render, redirect
from .forms import RegisterForm, AgendaForm
from .models import Clients_Register, Trip_Agenda
from django.contrib import messages

def index(request):
    return render(request, 'agencia/index.html', {})

def client_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, "Registro realizado com sucesso!")
                return redirect('sucessfull_register')
            except Exception as e:
                messages.error(request, f"Ocorreu um erro ao salvar o registro: {e}")
        else:
            messages.error(request, "O formulário contém erros. Por favor, corrija-os e tente novamente.")
    else:
        form = RegisterForm()
    
    return render(request, 'agencia/client_register.html', {'form': form})

def register_sucess(request):
    return render(request, 'agencia/sucessfull_register.html', {})

def travel_register(request):        
    if request.method == "POST":
        form = AgendaForm(request.POST)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.save()
                return redirect('sucessfull_booking',)
            except Exception as e:
                messages.error(request, f"Ocorreu um erro ao salvar o registro da viagem: {e}")
        else:
            messages.error(request, "O formulário contém erros. Por favor, corrija-os e tente novamente.")
    else:
        form = AgendaForm()
    return render(request, 'agencia/travel_register.html', {'form': form})     

def sucessfull_booking(request):
    return render(request, 'agencia/sucessfull_booking.html', {})  