from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .import views

urlpatterns = [
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('account/register', views.UserCreate.as_view()),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('products/', views.Product_ListView.as_view()),
    path('productsbytypes/<type>/', views.typeProduct_ListView.as_view()),
    path('productsbybrands/<type>/', views.typeProduct_ListView.as_view()),
    path('products/<int:pk>/', views.SingleProduct_ListView.as_view()),
    path('typeofproduct/', views.TypesofAllProductView.as_view()),
    path('typeofproduct/<int:pk>/', views.TypesofProductView.as_view()),

    path('slider/', views.SliderView.as_view()),
    path('slider/<int:pk>/', views.AllSliderView.as_view()),
]
