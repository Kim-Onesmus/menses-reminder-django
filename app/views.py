from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Client, Predict
from .forms import PredictForm


# Create your views here.
def Register(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       username = request.POST['username']
       gender = request.POST['gender']
       password = request.POST['password']
       password1 = request.POST['password1']
       
       if password == password1:
            if Client.objects.filter(username=username).exists():
               messages.error(request, 'Username already taken')
               return redirect('/')
            else:
               
               user = User.objects.create_user(first_name=first_name, username=username, password=password)
               user.save()
               
               client_details = Client.objects.create(first_name=first_name, username=username,gender=gender)
               client_details.save()
               
               messages.info(request, 'Account created')
               return redirect('login')
       else:
            messages.info(request, 'passwod dont match')
            return redirect('/')
    else:
        return render(request, 'app/register.html')
    return render(request, 'app/register.html')


def LogIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password,)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid password or username')
            return redirect('login')
    else:
        return render(request, 'app/login.html')
    return render(request, 'app/login.html')


@login_required(login_url='register')
def Home(request):
    return render(request, 'app/home.html')

@login_required(login_url='register')
def Prediction(request, pk):
    owner = Predict.objects.get(id=pk)
    form = PredictForm(initial={'owner':owner})
    if request.method == 'POST':
        form = PredictForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'app/predict.html', context)