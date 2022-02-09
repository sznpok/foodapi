from email.mime import base
from django.urls import path,include
from .views import FoodTypeViewset,CategoryMenuviewset, Orderviewset, SubCategoryMenuviewset, TableTypeviewset, Tableviewset
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('food-type',FoodTypeViewset,basename="food-type")
router.register('category-menu',CategoryMenuviewset,basename="category-menu")
router.register('subcategory-menu',SubCategoryMenuviewset,basename="subcategory-menu")
router.register('table-type',TableTypeviewset,basename="table-type")
router.register('table',Tableviewset,basename="table")
router.register('order',Orderviewset,basename="order")

urlpatterns = [
    path('',include(router.urls)),
    path('login/',jwt_views.TokenObtainPairView.as_view(),name="login"),
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
]