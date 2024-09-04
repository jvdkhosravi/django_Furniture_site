from django import forms
from .models import ContactForm


class ContactFormForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # اضافه کردن کلاس به فیلدها
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # اضافه کردن آیدی به فیلدها
        self.fields['first_name'].widget.attrs.update({'id': 'fname'})
        self.fields['last_name'].widget.attrs.update({'id': 'lname'})
        self.fields['email'].widget.attrs.update({'id': 'email'})
        self.fields['message'].widget.attrs.update({'id': 'message'})

    # اضافه کردن برچسب به فیلدها
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'email', 'message']