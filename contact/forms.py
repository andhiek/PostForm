from django import forms


class ContactForm(forms.Form):
    nama = forms.CharField(max_length=50)
    email = forms.EmailField()
    alamat = forms.CharField(
        widget=forms.Textarea()
    )
