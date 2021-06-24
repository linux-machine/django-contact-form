from django.test import TestCase
from django.urls import reverse


class ContactFormViewTests(TestCase):

    def test_send_with_valid_data_and_captcha(self):
        valid_data = {
            'name': 'Test',
            'from_email': 'test@example.com',
            'phone': '12223334455',
            'subject': 'Test subject',
            'message': 'Test message',
        }
        contact_url = reverse('contact:contact_form')
        response = self.client.post(contact_url, data=valid_data)
        self.assertEqual(response.status_code, 302)

    def test_send_with_invalid_data_and_captcha(self):
        invalid_data = {
            'name': 'Test',
            'from_email': 'test@example.com',
            'phone': 'aaaaaaa',
            'subject': 'Test subject',
            'message': 'Test message',
        }
        contact_url = reverse('contact:contact_form')
        response = self.client.post(contact_url, data=invalid_data)
        self.assertEqual(response.status_code, 400)
