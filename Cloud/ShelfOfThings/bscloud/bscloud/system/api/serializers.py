__author__ = 'Victor Polevoy'


from rest_framework import routers, serializers, viewsets, decorators
from bscloud.models import Products, Product, Board, Jobs


class ProductsSerializer(serializers.ModelSerializer):
    # board_id = serializers.RelatedField()
    # product_id = serializers.RelatedField()
    board_id = serializers.CharField(required=True, max_length=200)
    product_id = serializers.CharField(required=True, max_length=200)

    class Meta:
        model = Products
        fields = ('board_id', 'product_id')


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    # @decorators.detail_route(['delete'])
    # def destroy(self, request, pk=None):
    #     pass


class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(required=True, max_length=200)
    name = serializers.CharField(required=True, max_length=200, read_only=False)
    additional_info = serializers.CharField(required=True, max_length=2000)

    class Meta:
        model = Product
        fields = ('product_id', 'name', 'additional_info')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BoardSerializer(serializers.ModelSerializer):
    board_id = serializers.CharField(required=True, max_length=200)
    board_name = serializers.CharField(required=True, max_length=200, read_only=False)

    class Meta:
        model = Board
        fields = ('board_id', 'board_name')


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class JobsSerializer(serializers.ModelSerializer):
    job_type = serializers.IntegerField(required=True)
    # board_id = serializers.RelatedField()
    # product_id = serializers.RelatedField()
    # dont need
    # board_id = serializers.CharField(required=True, max_length=200)
    product_id = serializers.CharField(required=True, max_length=200)

    class Meta:
        model = Jobs
        fields = ('job_type', 'product_id')


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer


class SerializersRouter():
    @staticmethod
    def get_router():
        router = routers.DefaultRouter()
        router.register(r'products', ProductsViewSet)
        router.register(r'product', ProductViewSet)
        router.register(r'board', BoardViewSet)
        router.register(r'jobs', JobsViewSet)

        return router