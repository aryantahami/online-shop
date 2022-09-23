from django.urls import path
from .views import ProductListView, ProductDetailView, CommentCreateView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
    path('hello/', views.test_translation),
]
