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
from .forms import ConstantForm, CustomUserCreationForm

@login_required
def owner_dashboard(request):
    if request.user.user_type != 'owner':
        return redirect('dashboard')

    form_user = CustomUserCreationForm()
    constants = Constant.objects.all()
    forms_constant = []

    if request.method == 'POST':
        if 'create_user' in request.POST:
            form_user = CustomUserCreationForm(request.POST)
            if form_user.is_valid():
                form_user.save()
                return redirect('owner_dashboard')
        else:
            constant_id = request.POST.get('constant_id')
            constant = Constant.objects.get(pk=constant_id)
            form_constant = ConstantForm(request.POST, instance=constant, initial={'edit_mode': True})
            if form_constant.is_valid():
                if form_constant.cleaned_data['edit_mode']:
                    if constant.name not in ["Накладные расходы на 1 час фонда рабочего времени (руб.)"]:
                        constant.value = form_constant.cleaned_data['value']
                    constant.comment = form_constant.cleaned_data['comment']
                    constant.save()
                return redirect('owner_dashboard')
    else:
        for constant in constants:
            form_constant = ConstantForm(instance=constant, initial={'edit_mode': False})
            forms_constant.append((constant, form_constant))

    return render(request, 'Accounting_button/owner_dashboard.html', {
        'form_user': form_user,
        'constants_forms': forms_constant,
        'user': request.user
    })

