from django import forms

from vetsite.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            'message': forms.Textarea(attrs={'placeholder': 'Сообщение', 'cols': 30, 'rows': 9, 'class': 'w-100'}),
        }
