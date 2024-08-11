from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone',

    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error(
            'first_name', ValidationError('Mensagem de erro', code='invalid')
        )
        return super().clean()

def create(request):
    if request.method == 'POST':
        context = { 'form': ContactForm(data=request.POST) }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
         'form': ContactForm() 
        }

    return render(
        request,
        'contact/create.html',
        context
    )

    