from django.shortcuts import render, redirect
from .forms import RegisterForm, AgendaForm, SearchClientForm, SearchTravelForm
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

#def show_clients(request):
#    clientes = Clients_Register.objects.all()
#    return render(request, 'agencia/clients_list.html', {'clientes': clientes})

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


def search(request):
    form = SearchClientForm()
    results = None
    trips = None

    if request.method == 'GET':
        form = SearchClientForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
           
            results = Clients_Register.objects.filter(cpf__icontains=query) | Clients_Register.objects.filter(rg__icontains=query)
            if results.exists():
                
                client = results.first()
                trips = Trip_Agenda.objects.filter(id_client=client)

    return render(request, 'agencia/search.html', {'form': form, 'results': results, 'trips': trips})

