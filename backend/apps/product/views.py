from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from .models import SubCategory, Category, Product, BanerImage

def get_subcategories(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))

    return HttpResponse(json.dumps(result), content_type="application/json")

class IndexPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baners = BanerImage.objects.all()
        if len(baners) > 6:
            baners = baners[:6]
        context['baners'] = baners
        return context

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 6

    def get_queryset(self, **kwargs):
        print(self.kwargs)
        category_slug = self.kwargs.get('slug')
        subcategory_slug = self.kwargs.get('subcategory_slag')
        if subcategory_slug:
            products = Product.objects.filter(is_active=True, subcategory_slug=subcategory_slug)
        elif category_slug:
            products = Product.objects.filter(is_active=True, category__slug=category_slug)
        else:
            products = Product.objects.filter(is_active=True)
        return products

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
