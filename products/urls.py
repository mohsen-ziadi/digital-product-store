from django.urls import path
from . import views

app_name='products'
urlpatterns = [
    path('products/',ProductListView.as_view()),
]