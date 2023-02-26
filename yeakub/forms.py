from django import forms

from yeakub.models import AdminContact

class AdminContactForm(forms.Form):
    name = forms.CharField(label='write your name', required=True,max_length=100)
    email = forms.EmailField(label='write your name',required=True,max_length=100)
    subject = forms.CharField(label='write your name',required=True,max_length=300)
    message = forms.CharField(label='write your name',required=True,widget=forms.Textarea)

    class Meta:
        model = AdminContact
        fields = [
            'name',
            'email',
            'subject',
            'message',
            
        ]

    def __init__(self, *args, **kwargs):
        super(AdminContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail Address'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'