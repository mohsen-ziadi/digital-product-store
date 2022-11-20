from django.urls import path
from .views import *

app_name='products'
urlpatterns = [
    path('product/',ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/',ProductDetailView.as_view(), name="product-detail"),
    path('category/',CategoryListView.as_view(), name="category-list"),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
]