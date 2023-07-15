from django import forms

class ContactForm(forms.Form):
    sender_name = forms.CharField(max_length=255)
    from_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

