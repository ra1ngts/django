from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response

from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('-id')


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_products_list(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_list')
    else:
        form = ProductForm()
    return render(request, 'index.html', {'form': form})
