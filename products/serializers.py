from rest_framework import serializers
from  .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description' , 'avatar')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('title','file')

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('title', 'description','avatar','categories','files')