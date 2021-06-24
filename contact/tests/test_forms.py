from django.test import TestCase

from ..forms import ContactForm


class ContactFormTests(TestCase):

    def test_form_with_valid_data(self):
        valid_data = {
            'name': 'Test',
            'from_email': 'test@example.com',
            'phone': '12223334455',
            'subject': 'Test subject',
            'message': 'Test message',
        }
        form = ContactForm(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        invalid_data = {
            'name': 'Test',
            'from_email': 'test@example.com',
            'phone': 'aaaaaaa',
            'subject': 'Test subject',
            'message': 'Test message',
        }
        form = ContactForm(data=invalid_data)
        self.assertFalse(form.is_valid())
