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
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def director_dashboard(request):
    return render(request, 'Accounting_button/director_dashboard.html', {'user': request.user})

# Дашборд собственника с обработкой формы создания пользователя и редактирования констант
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def owner_dashboard(request):
    return render(request, 'Accounting_button/owner_dashboard.html', {'user': request.user})


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

@login_required
def client_create(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('client_list')
    else:
        client_form = ClientForm()
    return render(request, 'Accounting_button/client_create.html', {'client_form': client_form})

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return HttpResponseRedirect(reverse('client_list'))
    return render(request, 'Accounting_button/client_confirm_delete.html', {'client': client})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Constant
from .forms import ConstantForm

@login_required
def constant_list(request):
    constants = Constant.objects.all()
    return render(request, 'Accounting_button/constant_list.html', {'constants': constants})

@login_required
def constant_edit(request, constant_id):
    constant = get_object_or_404(Constant, id=constant_id)
    if request.method == 'POST':
        form = ConstantForm(request.POST, instance=constant)
        if form.is_valid():
            form.save()
            return redirect('constant_list')
    else:
        form = ConstantForm(instance=constant)
    return render(request, 'Accounting_button/constant_edit.html', {'form': form, 'constant': constant})

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import WorkType
from .forms import WorkTypeForm

class WorkTypeListView(ListView):
    model = WorkType
    template_name = 'worktype_list.html'


class WorkTypeDeleteView(DeleteView):
    model = WorkType
    template_name = 'Accounting_button/worktype_confirm_delete.html'
    success_url = reverse_lazy('worktype_list')

from django.views.generic import CreateView, UpdateView
from .models import WorkType
from .forms import WorkTypeForm


class WorkTypeCreateView(CreateView):
    model = WorkType
    form_class = WorkTypeForm
    template_name = 'Accounting_button/worktype_form.html'
    success_url = reverse_lazy('worktype_list')


class WorkTypeUpdateView(UpdateView):
    model = WorkType
    form_class = WorkTypeForm
    template_name = 'Accounting_button/worktype_form.html'
    success_url = reverse_lazy('worktype_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Добавляем пользователя в контекст
        return context

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UnusualOperationLogForm
from .models import UnusualOperationLog, Constant
from django.contrib.auth.decorators import login_required

@login_required
def unusual_operation_log_list(request):
    logs = UnusualOperationLog.objects.all()
    return render(request, 'Accounting_button/unusual_operation_log_list.html', {'logs': logs})

@login_required
def create_unusual_operation_log(request):
    chief_accountant_cost = Constant.objects.get(name="Стоимость минуты рабочего времени Главного бухгалтера").value
    accountant_cost = Constant.objects.get(name="Стоимость минуты рабочего времени бухгалтера").value

    if request.method == "POST":
        form = UnusualOperationLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.author = request.user
            if log.price_category == 'Главный бухгалтер':
                cost_per_minute = chief_accountant_cost
            elif log.price_category == 'Бухгалтер':
                cost_per_minute = accountant_cost
            else:
                cost_per_minute = 0
            log.operation_cost = cost_per_minute * log.duration_minutes
            log.save()
            return redirect('unusual_operation_log_list')
    else:
        form = UnusualOperationLogForm()

    return render(request, 'Accounting_button/unusual_operation_log_form.html', {
        'form': form,
        'chief_accountant_cost': chief_accountant_cost,
        'accountant_cost': accountant_cost,
    })

@login_required
def unusual_operation_log_delete(request, pk):
    log = get_object_or_404(UnusualOperationLog, pk=pk)
    if request.method == 'POST':
        log.delete()
        return redirect('unusual_operation_log_list')
    return render(request, 'Accounting_button/unusual_operation_log_confirm_delete.html', {'log': log})

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UnusualOperationLog, Constant
from .forms import UnusualOperationLogForm

@login_required
def unusual_operation_log_update(request, pk):
    log = get_object_or_404(UnusualOperationLog, pk=pk)
    chief_accountant_cost = Constant.objects.get(name="Стоимость минуты рабочего времени Главного бухгалтера").value
    accountant_cost = Constant.objects.get(name="Стоимость минуты рабочего времени бухгалтера").value

    if request.method == 'POST':
        form = UnusualOperationLogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            if log.price_category == 'Главный бухгалтер':
                cost_per_minute = chief_accountant_cost
            elif log.price_category == 'Бухгалтер':
                cost_per_minute = accountant_cost
            else:
                cost_per_minute = 0
            log.operation_cost = cost_per_minute * log.duration_minutes
            log.save()
            return redirect('unusual_operation_log_list')
    else:
        form = UnusualOperationLogForm(instance=log)
    return render(request, 'Accounting_button/unusual_operation_log_form.html', {
        'form': form,
        'chief_accountant_cost': chief_accountant_cost,
        'accountant_cost': accountant_cost,
    })


from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import StandardOperationLog
from .forms import StandardOperationLogForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.utils.timezone import now
from django.db.models import Sum
from .models import StandardOperationLog

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import StandardOperationLog
from .forms import StandardOperationLogForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class StandardOperationLogListView(ListView):
    model = StandardOperationLog
    template_name = 'Accounting_button/standard_operation_log_list.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = now().date()
        month_start = today.replace(day=1)

        context['time_norm_today'] = StandardOperationLog.objects.filter(timestamp__date=today).aggregate(Sum('time_norm'))['time_norm__sum'] or 0
        context['time_norm_month'] = StandardOperationLog.objects.filter(timestamp__date__gte=month_start).aggregate(Sum('time_norm'))['time_norm__sum'] or 0
        return context

@method_decorator(login_required, name='dispatch')
class StandardOperationLogCreateView(CreateView):
    model = StandardOperationLog
    form_class = StandardOperationLogForm
    template_name = 'Accounting_button/standard_operation_log_form.html'
    success_url = reverse_lazy('standard_operation_log_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class StandardOperationLogUpdateView(UpdateView):
    model = StandardOperationLog
    form_class = StandardOperationLogForm
    template_name = 'Accounting_button/standard_operation_log_form.html'
    success_url = reverse_lazy('standard_operation_log_list')

@method_decorator(login_required, name='dispatch')
class StandardOperationLogDeleteView(DeleteView):
    model = StandardOperationLog
    template_name = 'Accounting_button/standard_operation_log_confirm_delete.html'
    success_url = reverse_lazy('standard_operation_log_list')


from django.shortcuts import render, get_object_or_404, redirect
from .models import DeviationLog, Client
from .forms import DeviationLogForm
from django.contrib.auth.decorators import login_required

@login_required
def deviation_log_list(request):
    logs = DeviationLog.objects.all()
    return render(request, 'Accounting_button/deviation_log_list.html', {'logs': logs})

@login_required
def create_deviation_log(request):
    if request.method == "POST":
        form = DeviationLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.author = request.user
            if log.client:
                log.inn = log.client.inn
            log.save()
            return redirect('deviation_log_list')
    else:
        form = DeviationLogForm()
    return render(request, 'Accounting_button/deviation_log_form.html', {'form': form})

@login_required
def update_deviation_log(request, pk):
    log = get_object_or_404(DeviationLog, pk=pk)
    if request.method == 'POST':
        form = DeviationLogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            if log.client:
                log.inn = log.client.inn
            log.save()
            return redirect('deviation_log_list')
    else:
        form = DeviationLogForm(instance=log)
    return render(request, 'Accounting_button/deviation_log_form.html', {'form': form})

@login_required
def delete_deviation_log(request, pk):
    log = get_object_or_404(DeviationLog, pk=pk)
    if request.method == 'POST':
        log.delete()
        return redirect('deviation_log_list')
    return render(request, 'Accounting_button/deviation_log_confirm_delete.html', {'log': log})

from django.shortcuts import render
from django.db.models import Sum
from .models import StandardOperationLog
from datetime import datetime, timedelta

def standard_operations_report(request):
    today = datetime.today()
    start_of_day = datetime.combine(today, datetime.min.time())
    start_of_month = datetime(today.year, today.month, 1)

    # Суммируем time_norm за текущий день и за текущий месяц
    time_norm_today = StandardOperationLog.objects.filter(timestamp__gte=start_of_day).aggregate(Sum('time_norm'))['time_norm__sum'] or 0
    time_norm_month = StandardOperationLog.objects.filter(timestamp__gte=start_of_month).aggregate(Sum('time_norm'))['time_norm__sum'] or 0

    # Суммируем operation_cost за текущий день и за текущий месяц
    operation_cost_today = StandardOperationLog.objects.filter(timestamp__gte=start_of_day).aggregate(Sum('operation_cost'))['operation_cost__sum'] or 0
    operation_cost_month = StandardOperationLog.objects.filter(timestamp__gte=start_of_month).aggregate(Sum('operation_cost'))['operation_cost__sum'] or 0

    context = {
        'time_norm_today': time_norm_today,
        'time_norm_month': time_norm_month,
        'operation_cost_today': operation_cost_today,
        'operation_cost_month': operation_cost_month,
    }

    return render(request, 'Accounting_button/standard_operations_report.html', context)



