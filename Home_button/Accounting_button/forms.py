from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Constant, Client, WorkType, UnusualOperationLog, StandardOperationLog, DeviationLog

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'user_type', 'password1', 'password2')

class ConstantForm(forms.ModelForm):
    class Meta:
        model = Constant
        fields = ['value', 'comment']
        widgets = {
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ConstantForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs.update({'id': f'id_value_{self.instance.id}'})
        self.fields['comment'].widget.attrs.update({'id': f'id_comment_{self.instance.id}'})

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'org_form', 'inn', 'contract_price', 'tax_system', 'contract_details', 'contact_person', 'phone', 'email', 'postal_address', 'comments']

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'user_type']

class WorkTypeForm(forms.ModelForm):
    class Meta:
        model = WorkType
        fields = ['name', 'time_norm', 'price_category', 'comments']

# forms.py
from django import forms
from .models import UnusualOperationLog, Client

class UnusualOperationLogForm(forms.ModelForm):
    class Meta:
        model = UnusualOperationLog
        fields = ['operation_content', 'duration_minutes', 'client', 'price_category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.all()
        self.fields['client'].widget.attrs.update({'class': 'form-control'})
        self.fields['client'].choices = [
            (client.id, f"{client.id} - {client.name}") for client in Client.objects.all()
        ]

# forms.py
from django import forms
from .models import StandardOperationLog, WorkType, Client

class StandardOperationLogForm(forms.ModelForm):
    class Meta:
        model = StandardOperationLog
        fields = ['client', 'worktype', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['worktype'].queryset = WorkType.objects.all()
        self.fields['worktype'].widget.attrs.update({'class': 'form-control'})

        # Добавляем номера к названиям работы
        self.fields['worktype'].choices = [
            (wt.id, f"{wt.id} - {wt.name}") for wt in WorkType.objects.all()
        ]

        self.fields['client'].queryset = Client.objects.all()
        self.fields['client'].widget.attrs.update({'class': 'form-control'})

        # Добавляем номера к названиям клиентов
        self.fields['client'].choices = [
            (client.id, f"{client.id} - {client.name}") for client in Client.objects.all()
        ]


class DeviationLogForm(forms.ModelForm):
    class Meta:
        model = DeviationLog
        fields = ['content', 'reason', 'client', 'comments']
