from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from apps.models import Product


def index_view(request):
    search = request.GET.get('search')
    products = Product.objects.filter(category__name__icontains=search)
    context = {
        "products": products,
    }
    return render(request, 'apps/index.html', context)


def main_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'apps/main.html', context)


class Main(TemplateView):
    template_name = 'apps/index.html'

