# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'size': '40', 'class': 'form-control', 'placeholder': u'Введите тему сообщения'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control',
                                                            'placeholder': u'Введите ваш email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': u'Введите текст сообщения'}))
    copy = forms.BooleanField(required=False)
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
