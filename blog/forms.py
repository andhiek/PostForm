from django import forms


from .models import PostModel


class PostForms(forms.Form):
    judul = forms.CharField(max_length=50)
    isi = forms.CharField(
        widget=forms.Textarea()
    )
    category = forms.CharField(max_length=100)
    
    
    def clean_judul(self):
        judul_input = self.cleaned_data.get('judul')
        
        if PostModel.objects.filter(judul=judul_input).exists():
            raise forms.ValidationError(judul_input + ' tidak bisa di posting')
        return judul_input
