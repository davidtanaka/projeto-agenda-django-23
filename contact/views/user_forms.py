from django.shortcuts import redirect, render

from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            # return redirect('user:register')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )