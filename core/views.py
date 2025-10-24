from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Kit
from .forms import KitForm


def home(request):
    return render(request, 'home.html') #public homepage
# Create your views here.
@login_required
def dashboard(request):
    kits = Kit.objects.all().order_by('name')
    return render(request, 'dashboard.html', {'kits': kits})

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
    return render(request, 'update_kit.html', {'form': form, 'kit': kit})
