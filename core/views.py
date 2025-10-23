from django.shortcuts import render
from .models import Kit
from .forms import KitForm


# Create your views here.
def Dashboard(request):
    kits = Kit.objects.all().order_by('name')
    return render(request, 'core/dashboard.html', {'kits': kits})

