from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Kit
from .forms import KitForm, PostMortForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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
    theme = request.session.get('theme', 'light')
    sort_option = request.GET.get('sort', 'name')  # default sort
    if sort_option == 'latest':
        kits = Kit.objects.all().order_by('-updated_at')  # ✅ sort by last update
    elif sort_option == 'number':
        kits = Kit.objects.all().order_by('name')
    else:
        kits = Kit.objects.all()

    return render(request, 'core/dashboard.html', {'kits': kits, 'sort_option': sort_option, 'theme': theme})


@login_required
def create_postmortem(request):
    if request.method == 'POST':
        form = PostMortForm(request.POST)
        if form.is_valid():
            postmortem = form.save()
            # update linked kit
            kit = postmortem.kit
            kit.issues = postmortem.issues
            kit.needs_restock = bool(postmortem.restock)
            kit.save()

            return redirect('dashboard')
    else:
        form = PostMortForm()
    return render(request, 'core/postmortem_form.html', {'form': form})


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


def view_kit(request, kit_id):
    kit = get_object_or_404(Kit, id=kit_id)
    postmortems = kit.postmortem_set.all().order_by('-event_date')
    latest_pm = postmortems.first()
    return render(request, 'core/view_kit.html', {
        'kit': kit,
        'postmortems': postmortems,
        'latest_pm': latest_pm
    })


def index(request):
    theme = request.session.get('theme', 'light')
    return render(request, 'index.html', {'theme': theme})


def toggle_theme(request):
    current = request.session.get('theme', 'light')
    request.session['theme'] = 'dark' if current == 'light' else 'light'
    return redirect(request.META.get('HTTP_REFERER', '/'))


@csrf_exempt
def toggle_restock(request, kit_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        kit = Kit.objects.get(id=kit_id)
        kit.needs_restock = data.get('needs_restock', False)
        kit.save()
        return JsonResponse({'success': True, 'needs_restock': kit.needs_restock})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def save_restock_status(request, kit_id):
    if request.method == 'POST':
        kit = get_object_or_404(Kit, id=kit_id)
        # If the checkbox is present, it's checked → means "fully stocked"
        kit.needs_restock = not bool(request.POST.get('needs_restock'))
        kit.save()
    return redirect('dashboard')
