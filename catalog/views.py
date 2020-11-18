from django.shortcuts import render
from .models import Catalog, Service


def catalog_man(request):
    service = Service.objects.filter(gender='man').order_by('price_man_all')
    context_catalog = {'service': service}
    return render(request, 'catalog/catalog_man.html', context_catalog)


def catalog_woman(request):
    service = Service.objects.filter(gender='woman').order_by('price_1')
    context_catalog = {'service': service}
    return render(request, 'catalog/catalog_woman.html', context_catalog)


def price(request):
    service_woman = Service.objects.filter(gender='woman').order_by('price_1')
    service_man = Service.objects.filter(gender='man').order_by('price_man_all')
    context_catalog = {'service_woman': service_woman,
                       'service_man': service_man}
    return render(request, 'catalog/price.html', context_catalog)