from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy


class EmailMessage(models.Model):
    name = models.CharField(_('Sender Name'), max_length=40)
    from_email = models.EmailField(_('Sender E-mail'), max_length=255)
    phone = models.CharField(_('Sender Phone Number'), max_length=15, null=True, blank=True)
    subject = models.CharField(_('Message Subject'), max_length=255, null=True, blank=True)
    message = models.TextField(_('Message Text'))
    sent = models.DateTimeField(_('Sent'), auto_now_add=True)

    class Meta:
        verbose_name = _('E-mail Message')
        verbose_name_plural = _('E-mail Messages')

    def __str__(self):
        return str(format_lazy(_('Message from {name}'), name=self.name))
