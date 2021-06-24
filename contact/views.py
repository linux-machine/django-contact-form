from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _
from django.utils.text import format_lazy
from django.urls import reverse_lazy
from django.http import JsonResponse

from .forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact:contact_form')
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if request.recaptcha_is_valid and form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)

        form.send_email()

        form.save()

        name = form.cleaned_data['name']

        if self.request.is_ajax():
            data = {
                'success_msg': format_lazy(_('Thank you, {name}! I\'ll reply you soon...'), name=name)
            }
            return JsonResponse(data)
        else:
            return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            if self.request.recaptcha_is_valid:
              return JsonResponse(form.errors, status=400)
            else:
                return JsonResponse({
                    'detail': _('Please confirm that you are not a robot.')}, status=400)
        else:
            response.status_code = 400
            return response


contact_form_view = ContactFormView.as_view()
