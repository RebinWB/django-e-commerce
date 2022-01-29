from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control input-item", "placeholder": "Your Name"}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control input-item", "placeholder": "Email"}))

    subject = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control input-item", "placeholder": "Subject"}))

    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control textarea-item", "placeholder": "Message"}))
