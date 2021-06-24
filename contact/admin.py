from django.contrib import admin

from .models import EmailMessage


class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'sent', 'name', 'from_email', 'phone', 'subject')
    search_fields = ('name', 'from_email')


admin.site.register(EmailMessage, EmailMessageAdmin)
