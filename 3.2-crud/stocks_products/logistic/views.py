from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # Переделал зарезервированное слово search на слово products
    filter_backends = [SearchFilter]
    # Поиск по названию или описанию поля с частичным или полным совпадением без учета регистра чтобы могли искать
    # например таким образом: ..stocks/?products=огуре
    search_fields = ['products__title', 'products__description']

