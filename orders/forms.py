from django import forms
from orders.models import OrderDetails


class OrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput())

    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 1,
            }),
        initial=1)


class OrderDetailsForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
            }))

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "First Name",
            }))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Last Name",
            }))

    class Meta:
        model = OrderDetails
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone",
            "province",
            "city",
            "address",
            "company_name",
            "postcode",
        ]

        widgets = {
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number",
            }),

            "province": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Province"
            }),

            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "City"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Address",
                "cols": 30,
                "rows": 3,
            }),

            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name",
                "required": False
            }),

            "postcode": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Post Code"
            }),
        }
