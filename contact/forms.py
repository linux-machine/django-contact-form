import re

from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.conf import settings

from .models import EmailMessage


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, min_length=2, max_length=40, label=_('Name'),
                           widget=forms.TextInput(attrs={'placeholder': _('What\'s your name?'),
                                                         'class': 'form-group textinput textInput form-control'}, ),
                           error_messages={'required': _('Name field is required.')},)
    phone = forms.CharField(required=False, min_length=7, max_length=15, label=_('Phone Number'),
                            widget=forms.TextInput(attrs={'placeholder': '12223334455',
                                                          'class': 'form-group textinput textInput form-control'}))

    class Meta:
        model = EmailMessage
        exclude = ['sent',]
        widgets = {
            'from_email': forms.EmailInput(attrs={'placeholder': 'user@domain.com',
                                                  'class': 'form-group textinput textInput emailinput form-control',}),
            'subject': forms.TextInput(attrs={'placeholder': _('Message subject'),
                                        'class': 'form-group textinput textInput form-control',}),
            'message': forms.Textarea(attrs={'placeholder': _('Your message'),
                                       'class': 'form-group textinput textInput form-control',}),

        }
        labels = {
            'from_email': _('Your E-mail'),
            'subject': _('Subject'),
            'message': _('Message'),
        }
        error_messages = {
            'message': {
                'required': _('Message field is required.'),
            }
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        pattern = r'^[a-zA-Zа-яА-ЯёЁ]+( +[a-zA-Zа-яА-ЯёЁ]+)*$'
        if not re.match(pattern, name):
            self.add_error('name', _('A name must contain only letters and spaces.'))
        return name

    def clean_from_email(self):
        from_email = self.cleaned_data['from_email']
        return from_email.lower()

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = r'^\d+$'
        if not re.match(pattern, phone) and phone != '':
            self.add_error('phone', _('A phone number must contain only digits.'))
        return phone

    def send_email(self):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['from_email']
        phone = self.cleaned_data['phone']
        subject = self.cleaned_data['subject']
        message = format_lazy(_('{message}\n'
                                'From: {name} {from_email} {phone}'), message=self.cleaned_data['message'], name=name,
                              from_email=from_email, phone=phone)

        recipient_list = [manager[1] for manager in settings.MANAGERS]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
