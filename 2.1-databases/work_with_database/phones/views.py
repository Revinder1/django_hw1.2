from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = request.GET.get('sort', None)
    # Если у нас есть параметр sort в url, проверяем, есть ли параметр в словаре switcher и подставляем нужную
    # сортировку товара в вывод пользователю
    switcher = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    template = 'catalog.html'
    if sort_by in switcher.keys():
        phones = Phone.objects.all().order_by(switcher[sort_by])
    else:
        # Если параметра для сортировки нет, то возвращаем все результаты без сортировки
        phones = Phone.objects.all()

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # iexact - не чувствительный к регистру slug (insensitive)
    phone = Phone.objects.get(slug__iexact=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
