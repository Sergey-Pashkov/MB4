from django.shortcuts import render, redirect
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

# Список клиентов
@login_required
def client_list(request):
    clients = Client.objects.all()  # Получение всех клиентов из базы данных
    return render(request, 'Accounting_button/client_list.html', {'clients': clients})

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
