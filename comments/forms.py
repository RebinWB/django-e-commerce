from django import forms

class CommentForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    comment_text = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Write Your Comment Here"
    }))
