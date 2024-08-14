from django.shortcuts import  redirect, render

from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        context = { 'form': form }

        if form.is_valid():
            # contacts_test = form.save(commit=False) # Isso não vai salvar na base de dados
            # Mas com o código abaixo vou salvar essa váriavel:
            # contacts_test.show=False
            form.save()
            return redirect('contact:create')

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

    