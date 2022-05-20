import datetime

from django.shortcuts import render, redirect
from .models import Book


def index(request):
    return redirect('catalog')


def books_catalog_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)


def books_view(request, pub_date):
    template = 'books/books_list.html'

    try:
        pub_d = datetime.datetime.strptime(pub_date, '%Y-%m-%d')
        prev_date = Book.objects.filter(pub_date__lt=pub_d).order_by('-pub_date').first()
        next_date = Book.objects.filter(pub_date__gt=pub_d).order_by('pub_date').first()
        context = {
            'books': Book.objects.filter(pub_date__exact=pub_d),
            'prev_date': prev_date,
            'next_date': next_date,
        }
    except (TypeError, ValueError):
        context = {
            'books': Book.objects.order_by('pub_date').all()
        }
    return render(request, template, context)
    # if Book.objects.filter(pub_date=pub_date):
    #     context = {
    #         'books': Book.objects.filter(pub_date=pub_date),
    #     }
    #     return render(request, template, context)
    #


# < a
# href = "?{{ oldest_book.pub_date|date:"
# Y - m - d
# " }}" > Назад < / a >
