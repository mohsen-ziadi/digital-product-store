from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class ProductListView(APIView):

    def get(self,request):
        products = Product.objects.all()
        serializers = ProductSerializer(products,many=True)
        return Response(serializers.data)
