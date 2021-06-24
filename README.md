# django-contact-form

Это приложение предоставляет функции контактной формы для [Django](https://www.djangoproject.com/) сайта.
Шаблон формы создан с помощью [Bootstrap v4.3.1](https://getbootstrap.com/docs/4.3/getting-started/download/).

License: | MIT
-------- | ---

![broken link](https://github.com/linux-machine/django-contact-form/blob/master/docs/_static/contact_form.jpeg?raw=true)

* Заголовки письма: "Имя", "Ваш E-mail", "Номер телефона", "Тема" - чтобы легко ответить отправителю;
* "Сообщение" - поле для ввода сообщения;
* Используется [Google reCAPTCHA](https://www.google.com/recaptcha/admin#list) v2 для блокировки спам-роботов.


# Быстрый старт

## Зависимости

* [Python](https://www.python.org/downloads/) (3.5, 3.6, 3.7, 3.8, 3.9)
* [Django](https://www.djangoproject.com/download/) (2.2)
* [jQuery](https://code.jquery.com/jquery/) (3.2.1)


## Установка

1. Скачайте [django-contact-form-x.x.tar.gz](https://github.com/linux-machine/django-contact-form/releases)
 
2. Установите приложение в виртуальное окружение:

        $ pip install django-contact-form-x.x.tar.gz
        
3. Добавьте "contact" в список установленных приложений:

        INSTALLED_APPS = [
            ...
            'contact',
        ]    
    
4. Добавьте URLconf приложения в `urls.py` проекта:
    
        path('contact/', include('contact.urls', namespace='contact')),
        
5. Запустите `python manage.py migrate`, чтобы создать модель контактной формы.


## Настройки

Добавьте в `settings.py` проекта:

        ...   
        TEMPLATES = [
            {
                ...
                'OPTIONS': {
                    'context_processors': [
                        ...
                        'contact.utils.context_processors.google_recaptcha_site_key',
                    ],
                },
            },
        ]
        ...
        MANAGERS = ADMINS
        ...
        # Google reCAPTCHA
        # ------------------------------------------------------------------------------
        # for testing purpose only
        GOOGLE_RECAPTCHA_SECRET_KEY=6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe
        GOOGLE_RECAPTCHA_SITE_KEY=6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI 
    
    
## Пример использования

`views.py`

    ...
    from django.views.generic import TemplateView
    ...
    from contact.forms import ContactForm
    
    
    class MyAwesomeView(TemplateView):
        template_name = 'my_awesome_template.html'
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['form'] = ContactForm()
            return context
                       

`my_awesome_template.html`

    ...
    {% include "contact/contact_form.html" %}
    ...
    
    
## Удаление        
        
Чтобы удалить приложение из виртуального окружения, запустите команду:

    $ pip uninstall django-contact-form


## Основные команды
    
### Тесты

Чтобы запустить тесты, используйте команду:

    $ python manage.py test contact
