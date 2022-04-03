from django import forms
from django.forms import CharField, TextInput, NumberInput, EmailInput, Textarea
from orders.models import Order, Contact


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(1, 10)],
        coerce=int
    )
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'company', 'country', 'adress', 'zip',
                  'city', 'province', 'phone', 'email']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_name'

            }),
            'last_name': TextInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_last_name'

            }),
            'company': TextInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_company'

            }),
            'country': TextInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_country'

            }),
            'adress': TextInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_address'
            }),
            'zip': NumberInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_zipcode',
            }),
            'city': TextInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_city'
            }),
            'province': TextInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_province'

            }),
            'phone': NumberInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_phone',
            }),
            'email': EmailInput(attrs={
                'class': 'checkout_input',
                'id': 'checkout_email',
            }),

        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'subject', 'text', ]
        widgets = {
            'first_name': TextInput(attrs={
                'id': "contact_name",
                'class': "contact_input"
            }
            ),
            'last_name': TextInput(attrs={
                'id': "contact_last_name",
                'class': "contact_input"
            }
            ),
            'subject': TextInput(attrs={
                'id': "contact_company",
                'class': "contact_input"
            }
            ),
            'text': Textarea(attrs={
                'id': "contact_textarea",
                'class': "contact_input contact_textarea"
            }
            ),
        }
