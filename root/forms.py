from django import forms
from root.models import Contact, Newsletter


class NameForms(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=245)
    massage = forms.CharField(widget=forms.Textarea)
    
    
class ContactForm(forms.ModelForm):
    
    
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    
    
    class Meta:
        model = Newsletter
        fields = '__all__'