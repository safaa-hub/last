from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, LoginView

router = DefaultRouter()
router.register(r'registration', viewset=RegisterViewSet, basename='user')
router.register(r'login', viewset=LoginView, basename='user')

urlpatterns = router.urls
