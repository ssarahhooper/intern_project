from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Kit
from .forms import KitForm


def home(request):
    return render(request, 'core/home.html') #public homepage


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)             # log in right after signup
            return redirect('dashboard')     # go straight to dashboard
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
# Create your views here.
@login_required
def dashboard(request):
    kits = Kit.objects.all().order_by('name')
    return render(request, 'core/dashboard.html', {'kits': kits})

@login_required
def update_kit(request, pk):
    kit = Kit.objects.get(pk=pk)
    if request.method == 'POST':
        form = KitForm(request.POST, instance=kit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = KitForm(instance=kit)
    return render(request, 'core/update_kit.html', {'form': form, 'kit': kit})
