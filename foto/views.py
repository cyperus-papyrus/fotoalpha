# coding=utf-8
from django.utils import timezone
from .models import Foto, Category
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from ipware.ip import get_real_ip
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def show_404(request):
    return render(request, '404.html')


def index(request):
    fotos = Foto.objects.all
    categories = Category.objects.all()
    return render(request, 'foto/index.html', {'fotos': fotos, 'categories': categories})


def foto(request, url):
    post_foto = get_object_or_404(Foto, url=url)
    return render(request, 'foto/foto.html', {'foto': post_foto})


def allfoto(request):
    post_foto = Foto.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(post_foto, 6)
    page = request.GET.get('page')
    try:
        fotos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        fotos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        fotos = paginator.page(paginator.num_pages)
    return render_to_response('foto/gallery.html', {'foto': fotos})


def about(request):
    return render(request, 'foto/about.html')


def categories(request, category):
    fotos = Foto.objects.filter(category=category)
    name = Category.objects.filter(id=category)
    catg = Category.objects.all()
    return render(request, 'foto/category.html', {'fotos': fotos, 'categories': catg, 'category': name})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            message_to_user = message
            client_address = get_real_ip(request)
            message += '\n\n' + u'email отправителя: ' + sender + '\n' + u'ip отправителя: ' + client_address
            copy = form.cleaned_data['copy']

            recipient = ['melnikovalena@yandex.ru']
            u_recipient = []
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                u_recipient.append(sender)
            try:
                send_mail(subject, message, 'robot@rudut.ru', recipient)
                send_mail(subject, message_to_user, 'robot@rudut.ru', u_recipient)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'foto/thanks.html')
    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'foto/contact.html', {'form': form})
