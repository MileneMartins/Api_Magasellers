from django.urls import path
#from rest_framework.routers import SimpleRouter

from . import views


urlpatterns = [
    path('', views.SellerViewSet.as_view(), name ='seller-list'),
    path('<int:pk>/', views.SellerDetailViewSet.as_view(), name="seller-detail"),
    path('products/', views.ProductViewSet.as_view(),name='product-list'),
    path('<int:pk>/', views.ProductDetailViewSet.as_view(), name="product-detail")
]