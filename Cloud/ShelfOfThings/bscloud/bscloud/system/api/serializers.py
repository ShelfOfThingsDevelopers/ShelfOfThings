__author__ = 'Victor Polevoy'


from rest_framework import routers, serializers, viewsets, decorators, generics, filters
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
    product_id = serializers.CharField(required=True, max_length=200, blank=True)
    name = serializers.CharField(required=False, max_length=200, read_only=False, blank=True)
    additional_info = serializers.CharField(required=False, max_length=2000)

    class Meta:
        model = Product
        fields = ('product_id', 'name', 'additional_info')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_id'
    # filter_class = ProductFilter
    # filter_backends = (filters.DjangoFilterBackend, )
    # filter_fields = ('product_id', 'name')

    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #
    #     product_id = self.kwargs.get('pk')
    #
    #     print('pk: %s' % product_id)
    #
    #     if product_id:
    #         queryset = Product.objects.filter(product_id=product_id)
    #
    #     return queryset


class ProductByIdLookupView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        product_id = self.kwargs['product_id']
        # return Product.objects.filter(product__product_id=product_id)
        return Product.objects.filter(product_id=product_id)


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
    job_type = serializers.IntegerField(required=False, blank=True)
    # product_id = serializers.RelatedField(source='product_id')
    # dont need
    # board_id = serializers.CharField(required=True, max_length=200)
    product_id = serializers.CharField(max_length=200)
    status = serializers.BooleanField(required=False, blank=True)

    class Meta:
        model = Jobs
        fields = ('job_type', 'product_id', 'status')


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    lookup_field = 'product_id'


class SerializersRouter():
    @staticmethod
    def get_router():
        router = routers.DefaultRouter()
        router.register(r'products', ProductsViewSet)
        router.register(r'product', ProductViewSet)
        router.register(r'board', BoardViewSet)
        router.register(r'jobs', JobsViewSet)

        return router