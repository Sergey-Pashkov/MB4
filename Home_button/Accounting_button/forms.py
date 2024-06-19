from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Constant 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'user_type', 'password1', 'password2')



# Форма для редактирования констант
from django import forms
from .models import Constant

class ConstantForm(forms.ModelForm):
    edit_mode = forms.BooleanField(required=False, label='Редактировать', initial=False)

    class Meta:
        model = Constant
        fields = ['value', 'comment', 'edit_mode']
        widgets = {
            'value': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(ConstantForm, self).__init__(*args, **kwargs)
        if not self.initial.get('edit_mode'):
            self.fields['value'].widget.attrs['readonly'] = True
            self.fields['comment'].widget.attrs['readonly'] = True
        else:
            if self.instance.name == "Накладные расходы на 1 час фонда рабочего времени (руб.)":
                self.fields['value'].widget.attrs['readonly'] = True
            else:
                self.fields['value'].widget.attrs.pop('readonly', None)
            self.fields['comment'].widget.attrs.pop('readonly', None)
