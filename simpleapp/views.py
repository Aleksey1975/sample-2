from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'simpleapp/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context




from django.http import HttpResponse


def multiply(request):
   print(request.GET)
   print(request.GET.get('a'))
   print(type(request.GET.get('a')))

   number = request.GET.get('number')
   multiplier = request.GET.get('multiplier')

   try:
       result = int(number) * int(multiplier)
       html = f"<html><body>{number}*{multiplier}={result}</body></html>"
   except (ValueError, TypeError):
       html = f"<html><body>Invalid input.</body></html>"

   return HttpResponse(html)


class ProductDetail(DetailView):
    model = Product
    template_name = 'simpleapp/product.html'
    context_object_name = 'product'

