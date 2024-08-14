from turtle import textinput
from django.core.exceptions import ValidationError
from django import forms
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Aqui venho do init'
            }
        ),
        label='Primeiro nome',
        help_text='Texto de ajuda para seu usuário'
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widgets.attrs.update({
        #     'placeholder': 'Digite seu nome Init'
        # })

    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone',
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu nome',
                }
            )
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid')
            
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
             self.add_error(
                'first_name',
                ValidationError(
                    'ABC não é aceito', 
                    code = 'invalid'
                )
            )
        return first_name
