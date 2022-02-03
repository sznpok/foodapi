from django.urls import path,include
from .views import FoodTypeViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('food-type',FoodTypeViewset,basename="food-type")

urlpatterns = [
    path('',include(router.urls)),
]