from django import forms
from .models import Mailbox
from django_recaptcha.fields import ReCaptchaField

class MailboxForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Mailbox
        fields = ["mail_name", "mail_message", "captcha"]