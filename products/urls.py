from django.urls import path
from .views import *

app_name='products'
urlpatterns = [
    path('product/',ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/',ProductDetailView.as_view(), name="product-detail"),
    path('product/<int:product_id>/files/',FileListView.as_view(),name='file-list'),
    path('product/<int:product_id>/files/<int:pk>/',FileDetailView.as_view(),name="file-detail"),

    path('category/',CategoryListView.as_view(), name="category-list"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
]