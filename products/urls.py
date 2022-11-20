from django.urls import path
from .views import *

app_name='products'
urlpatterns = [
    path('',ProductListView.as_view(), name='product-list'),
    path('<int:pk>/',ProductDetailView.as_view(),name="product-detail")

]