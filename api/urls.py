from email.mime import base
from django.urls import path,include
from .views import FoodTypeViewset,CategoryMenuviewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('food-type',FoodTypeViewset,basename="food-type")
router.register('category-menu',CategoryMenuviewset,basename="category-menu")

urlpatterns = [
    path('',include(router.urls)),
]