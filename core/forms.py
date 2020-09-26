from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.core.validators import RegexValidator


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St',
        'class': 'md-form mb-5'
    }))
    apartment_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Apartment of suite',
        'class': 'md-form mb-5 '
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))

    zip = forms.CharField(max_length=5, validators=[RegexValidator(r'^[0-9]{5}$')])
    CCname = forms.CharField(max_length=100)
    CCnumber = forms.CharField(max_length=10, validators=[RegexValidator(r'^[0-9]{10}$')])
    expiration = forms.CharField(max_length=5, validators=[RegexValidator(r'(0[1-9]|10|11|12)/[0-9]{2}$')])
    cvv = forms.CharField(max_length=3, validators=[RegexValidator(r'^[0-9]{3}$')])
