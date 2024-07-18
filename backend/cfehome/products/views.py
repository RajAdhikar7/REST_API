
from rest_framework import generics

# Create your views here.

from .models import Product
from .serializers import ProductSerializer


'''
    ListCreateAPIView inherits from both ListAPIView and CreateAPIView, combining their functionality.

    GET Request: Used to list all instances of a model.
    POST Request: Used to create a new instance of the model.
'''
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # perform_create method in Django REST framework is a 
    # hook provided by the CreateAPIView class to allow you
    # to customize the object creation process.
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' (by default)

product_detail_view = ProductDetailAPIView.as_view() 

class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use this method
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view() 
