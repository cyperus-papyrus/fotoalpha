# coding=utf-8
from django.contrib import admin
from .models import Foto, Category


class FotoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('title', 'image', 'image_prev', 'text', 'published_date',
                       ('meta_description', 'category', 'url',))
        }),
        (u'Главная страница', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('is_in_mainpage',)
        }),
    )


class StackedItemInline(admin.StackedInline):
    classes = ('grp-collapse grp-open',)


class TabularItemInline(admin.TabularInline):
    classes = ('grp-collapse grp-open',)


admin.site.register(Foto, FotoAdmin)
admin.site.register(Category)
