from django.shortcuts import render, redirect
from .forms import RegisterForm, AgendaForm
from .models import Clients_Register, Trip_Agenda

def index(request):
    return render(request, 'agencia/index.html', {})

def client_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('sucessfull_register',)
    else:
        form = RegisterForm()
    return render(request, 'agencia/client_register.html', {'form': form})

def register_sucess(request):
    return render(request, 'agencia/sucessfull_register.html', {})