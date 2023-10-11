from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(label="sender")
    subject = forms.CharField(label="subject", max_length="150")
    message = forms.CharField(label="message", widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['sender'].widget.attrs['placeholder'] = 'Your email'
