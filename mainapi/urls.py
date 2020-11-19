from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet,product_list,buydish

router = routers.DefaultRouter()
router.register('users',UserViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('addpro/',product_list),
    path('buydish/<int:pk>/',buydish)
]
