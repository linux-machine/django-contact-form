import urllib3
import json

from django.conf import settings

http = urllib3.PoolManager()


def check_recaptcha(func):
    def wrap(request, *args, **kwargs):
        request.recaptcha_is_valid = None
        if request.method == 'POST':
            recaptcha_response = request.POST.get('recaptcha')
            body = 'secret={}&response={}'.format(settings.GOOGLE_RECAPTCHA_SECRET_KEY, recaptcha_response)
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            req = http.request(method='POST', url='https://www.google.com/recaptcha/api/siteverify', body=body, headers=headers)
            response = json.loads(req.data)
            if response['success']:
                request.recaptcha_is_valid = True
            else:
                request.recaptcha_is_valid = False
        return func(request, *args, **kwargs)

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap
