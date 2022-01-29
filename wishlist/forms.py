from django import forms

class WishlistForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput())
