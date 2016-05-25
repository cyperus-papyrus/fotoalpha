# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
import logging

logger = logging.getLogger(__name__)


class Category(models.Model):
    category = models.CharField(max_length=200, verbose_name=u'Название раздела')

    def __str__(self):
        return self.category

    def __unicode__(self):
        return smart_text(self.category)

    class Meta:
        app_label = 'foto'
        verbose_name = u'Раздел'
        verbose_name_plural = u'Разделы'


class Foto(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Название')
    image = models.ImageField(upload_to='foto/media/', default='/foto/media/default.jpg',
                              verbose_name=u'Фотография', help_text=u"Загрузите фотографию")
    text = RichTextUploadingField(blank=True, default='', verbose_name=u'Описание')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name=u'Дата публикации',
                                          help_text=u'Если оставить пустым - запись не будет доступна пользователям')

    image_prev = models.ImageField(upload_to='foto/media/', default='/foto/media/default.jpg',
                                   verbose_name=u'Превью', help_text=u"Загрузите превью фотографии")
    meta_description = models.CharField(max_length=200, verbose_name=u'Мета тег "description"')
    is_in_mainpage = models.BooleanField(default=False, verbose_name=u'Отображать на главной странице')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'Раздел')
    url = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name=u'URL страницы',
                           help_text="Начальный и закрывающий / вводить НЕ нужно. Допустимы только латинские буквы, \
                           а так же символы -, _")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return smart_text(self.title)

    class Meta:
        app_label = 'foto'
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'
