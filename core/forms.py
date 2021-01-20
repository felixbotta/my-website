from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-mail'}), required=True, label='')
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Assunto'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Mensagem'}), required=True)


