from turtle import textinput
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu primeiro nome'
            }))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widgets.attrs.update({
        #     'placeholder': 'Digite seu nome Init'
        # })

    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone',\
                'email', 'description', 'phone',\
                'picture'
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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3
    )

    last_name = forms.CharField(
        required=True,
        min_length=3
    )

    email = forms.EmailField(
        required=True,
        min_length=3
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',\
            'username', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', 
                ValidationError('Já existe uma conta com esse e-mail')
            )

        # if email == '':
        #     self.add_error(
        #         'email',
        #         ValidationError('campo obrigatorio')
        #     )


        return email
    
    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')
                
    #     if first_name == '':
    #         self.add_error('first_name', ValidationError('Campo obrigatorio')) 
    

    # def clean_last_name(self):
    #     last_name = self.cleaned_data.get('last_name')
                
    #     if last_name == '':
    #         self.add_error('last_name', ValidationError('Campo obrigatorio')) 
