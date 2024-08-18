from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from apps.models import Product, Category


def index_view(request):
    search = request.GET.get('search', '')  # Default to an empty string if no search term
    products = Product.objects.filter(category__name__icontains=search) if search else Product.objects.all()
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


class MainView(TemplateView):  # Renamed to avoid conflict with the function-based view
    template_name = 'apps/index.html'
