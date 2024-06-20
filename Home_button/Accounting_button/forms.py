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
