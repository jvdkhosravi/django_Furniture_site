from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactFormForm
from .models import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ContactUs:success')
    else:
        form = ContactFormForm()

    return render(request, 'ContactUs/contact.html', {'form': form})


def success_view(request):
    return render(request, 'ContactUs/success.html')
