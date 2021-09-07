from django.urls import path, include

from .views import (BrowseProductView, ProductBorrowedListView, ProductBoughtListView, ProductCreateView, ProductLentListView, ProductSoldListView, ProductUpdateView, ProductListView,
                    ProductDeleteView, SingleProductRetrieveView, ProductSellView, ProductRentView)

app_name = 'api'
urlpatterns = [
    # views for product owner
    path('create-product/', ProductCreateView.as_view()),
    path('list-product/', ProductListView.as_view()),
    path('get-product/<pk>/', SingleProductRetrieveView.as_view()),
    path('update-product/<pk>/', ProductUpdateView.as_view()),
    path('delete-product/<pk>/', ProductDeleteView.as_view()),

    # views for customer
    path('browse/', BrowseProductView.as_view()),
    path('buy-product/', ProductSellView.as_view()),
    path('rent-product/', ProductRentView.as_view()),

    # views for stats
    path('bought/', ProductBoughtListView.as_view()),
    path('sold/', ProductSoldListView.as_view()),
    path('borrowed/', ProductBorrowedListView.as_view()),
    path('lent/', ProductLentListView.as_view()),
]
