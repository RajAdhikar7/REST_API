
from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermission
from .models import Product
from .serializers import ProductSerializer
from api.authentication import TokenAuthentication

'''
    ListCreateAPIView inherits from both ListAPIView and CreateAPIView, combining their functionality.

    GET Request: Used to list all instances of a model.
    POST Request: Used to create a new instance of the model.
'''
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]



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
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

product_detail_view = ProductDetailAPIView.as_view() 

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()
            

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs): #HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    #create method in above post method  calls the perform_create method.
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method 

    if method == "GET":
        if pk is not None:
            #detail view 
            obj = get_object_or_404(Product , pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)
        #list view
        queryset = Product.objects.all() 
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if method == "POST":
        ## create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
