from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
