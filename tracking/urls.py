from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'tracking'
router = DefaultRouter()
router.register('firs', views.FIRViewset)
router.register('fir-status', views.FIRStatusViewset)
router.register('fir-status-all', views.FIRStatusAllViewset)


urlpatterns = [
    path('', include(router.urls)),
]
