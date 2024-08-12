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
        # cleaned_data = self.cleaned_data
        self.add_error(
            'first_name', ValidationError('Mensagem de erro', code='invalid')
        )
        return super().clean()
