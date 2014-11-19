__author__ = 'Victor Polevoy'


from rest_framework import routers, serializers, viewsets
from bscloud.models import Products, Product


class ProductsSerializer(serializers.ModelSerializer):
    board_id = serializers.CharField(required=True, max_length=200, read_only=False)
    product_id = serializers.CharField(required=True, max_length=200)

    class Meta:
        model = Products
        fields = ('board_id', 'product_id')


# ViewSets define the view behavior.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(required=True, max_length=200)
    name = serializers.CharField(required=True, max_length=200, read_only=False)
    additional_info = serializers.CharField(required=True, max_length=2000)

    class Meta:
        model = Product
        fields = ('product_id', 'name', 'additional_info')


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Routers provide an easy way of automatically determining the URL conf.
class SerializersRouter():
    @staticmethod
    def get_router():
        router = routers.DefaultRouter()
        router.register(r'products', ProductsViewSet)
        router.register(r'product', ProductViewSet)

        return router