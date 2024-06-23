from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ClientForm, LoginForm
from .models import Client

# Create your views here.

def main(request):
    return render(request, 'index.html')

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()  # Сохранение клиента
            auth_code = client.auth_code  # Получение авторизационного кода из сохраненного клиента
            return render(request, 'success.html', {'auth_code': auth_code})
    else:
        form = ClientForm()
    
    return render(request, 'client_form.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_code = form.cleaned_data['auth_code']
            client = get_object_or_404(Client, auth_code=auth_code)
            context = {
                'client': client
            }
            return render(request, 'client_details.html', context)
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})