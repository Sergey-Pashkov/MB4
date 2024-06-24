from django.shortcuts import render, get_object_or_404, redirect

from .models import CustomUser, Constant, Client
from .forms import CustomUserCreationForm, ConstantForm, ClientForm
from django.contrib.auth.decorators import login_required

# Проверка типа пользователя и перенаправление на соответствующий дашборд
@login_required
def dashboard(request):
    if request.user.user_type == 'accountant':
        return redirect('accountant_dashboard')
    elif request.user.user_type == 'director':
        return redirect('director_dashboard')
    elif request.user.user_type == 'owner':
        return redirect('owner_dashboard')

# Дашборд бухгалтера
@login_required
def accountant_dashboard(request):
    return render(request, 'Accounting_button/accountant_dashboard.html', {'user': request.user})

# Дашборд директора с обработкой формы создания пользователя и клиента
@login_required
def director_dashboard(request):
    if request.method == 'POST':
        # Обработка формы регистрации нового пользователя
        if 'register' in request.POST:
            user_form = CustomUserCreationForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                return redirect('director_dashboard')
        # Обработка формы создания нового клиента
        elif 'save_client' in request.POST:
            client_form = ClientForm(request.POST)
            if client_form.is_valid():
                client_form.save()
                return redirect('director_dashboard')
    else:
        user_form = CustomUserCreationForm()  # Инициализация пустой формы для создания пользователя
        client_form = ClientForm()  # Инициализация пустой формы для создания клиента
    
    return render(request, 'Accounting_button/director_dashboard.html', {
        'user_form': user_form,  # Передача формы создания пользователя в контекст
        'client_form': client_form,  # Передача формы создания клиента в контекст
        'user': request.user  # Передача текущего пользователя в контекст
    })

# Дашборд собственника с обработкой формы создания пользователя и редактирования констант
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


@login_required
def client_list(request):
    clients = Client.objects.all()
    total_clients = clients.count()  # Считаем общее количество клиентов
    return render(request, 'Accounting_button/client_list.html', {
        'clients': clients,
        'total_clients': total_clients  # Передаем общее количество клиентов в контекст
    })


@login_required
def client_edit(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'Accounting_button/client_edit.html', {'form': form, 'client': client})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def user_list(request):
    # Получаем всех пользователей
    users = CustomUser.objects.all()
    # Рендерим шаблон с пользователями
    return render(request, 'Accounting_button/user_list.html', {'users': users})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserChangeForm

@login_required
def user_edit(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'Accounting_button/user_edit.html', {'form': form, 'user': user})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

@login_required
def user_add(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Accounting_button/user_add.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser

@login_required
def user_delete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'Accounting_button/user_confirm_delete.html', {'user': user})
