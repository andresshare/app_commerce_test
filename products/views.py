#from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwars):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(ListView):
    template_name = "products/featured-detail.html"

    def get_queryset(self, *args, **kwars):
        request = self.request
        return Product.objects.all().featured()



class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data( *args, **kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwars):
        request = self.request
        return Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request,"products/list.html",context)

#DetailView
class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data( *args, **kwargs)
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #      instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #          raise Http404("Product_doesnt exists")
    #     return instance

    def get_queryset(self, *args, **kwars):
        request = self.request
        pk =self.kwars.get('pk')
        return Product.objects.filter(pk=pk)

def product_detail_view(request, pk=None, *args, **kwargs):
        #instance = Product.objects.get(pk=pk) #id
        # instance = Product.objects.get_by_id(pk)
        # qs = Product.objects.filter(id=pk)

        #print(qs)
        # if qs.exists() and qs.count() == 1:
        #    instance = qs.first()
        # else:
        #     raise Http404("Product_doesnt exists")
        # instance = get_object_or_404(Product,pk=pk)

        instance = Product.objects.get_by_id(pk)
        if instance is None:
             raise Http404("Product_doesnt exists")
        context = {
            'object': instance
        }
        return render(request, "products/detail.html", context)

