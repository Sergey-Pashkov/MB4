from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Constant

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

from .models import Client

# forms.py
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'org_form', 'inn', 'contract_price', 'tax_system', 'contract_details', 'contact_person', 'phone', 'email', 'postal_address', 'comments']


from django import forms
from .models import CustomUser

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'user_type']

from django import forms
from .models import Constant


class ConstantForm(forms.ModelForm):
    class Meta:
        model = Constant
        fields = ['value', 'comment']

from django import forms
from .models import WorkType


class WorkTypeForm(forms.ModelForm):
    class Meta:
        model = WorkType
        fields = ['name', 'time_norm', 'price_category', 'comments']

from django import forms
from .models import UnusualOperationLog, Client, WorkType

# forms.py
from django import forms
from .models import UnusualOperationLog


class UnusualOperationLogForm(forms.ModelForm):
    class Meta:
        model = UnusualOperationLog
        fields = ['operation_content', 'duration_minutes', 'client', 'price_category']


from .models import StandardOperationLog

class StandardOperationLogForm(forms.ModelForm):
    class Meta:
        model = StandardOperationLog
        fields = ['client', 'worktype']
