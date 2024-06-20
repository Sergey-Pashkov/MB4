'''''
@login_required
def owner_dashboard(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Accounting_button/owner_dashboard.html', {'form': form, 'user': request.user})

'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from .models import Constant
from .forms import ConstantForm, CustomUserCreationForm 


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
    return render(request, 'Accounting_button/accountant_dashboard.html', {'user': request.user})

@login_required
def director_dashboard(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Accounting_button/director_dashboard.html', {'form': form, 'user': request.user})

# Представление для дашборда собственника
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Constant
from .forms import CustomUserCreationForm, ConstantForm


@login_required
def owner_dashboard(request):
    if request.method == 'POST' and 'create_user' in request.POST:
        form_user = CustomUserCreationForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('owner_dashboard')
    else:
        form_user = CustomUserCreationForm()

    if request.method == 'POST' and 'constant_id' in request.POST:
        constant_id = request.POST.get('constant_id')
        constant = Constant.objects.get(id=constant_id)
        form_constant = ConstantForm(request.POST, instance=constant)
        if form_constant.is_valid():
            form_constant.save()
            return redirect('owner_dashboard')
    else:
        constants = Constant.objects.all()
        constants_forms = [(constant, ConstantForm(instance=constant)) for constant in constants]

    return render(request, 'Accounting_button/owner_dashboard.html', {
        'form_user': form_user,
        'constants_forms': constants_forms,
        'user': request.user,
    })
