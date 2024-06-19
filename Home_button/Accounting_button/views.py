from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Report, CustomUser
from .forms import CustomUserCreationForm

@login_required
def dashboard(request):
    if request.user.user_type == 'accountant':
        return redirect('accountant_dashboard')
    elif request.user.user_type == 'director':
        return redirect('director_dashboard')
    elif request.user.user_type == 'owner':
        return redirect('owner_dashboard')

@login_required
def accountant_dashboard(request):
    return render(request, 'Accounting_button/accountant_dashboard.html')

@login_required
def director_dashboard(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Accounting_button/director_dashboard.html', {'form': form})

@login_required
def owner_dashboard(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Accounting_button/owner_dashboard.html', {'form': form})


# Create your views here.
