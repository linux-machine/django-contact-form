from django.urls import path

from .views import contact_form_view
from .utils.decorators import check_recaptcha


app_name = 'contact'
urlpatterns = [
    path('', check_recaptcha(contact_form_view), name='contact_form'),
]
