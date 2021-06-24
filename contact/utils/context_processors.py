from django.conf import settings


def google_recaptcha_site_key(request):
    site_key = {'sitekey': settings.GOOGLE_RECAPTCHA_SITE_KEY}
    return site_key
