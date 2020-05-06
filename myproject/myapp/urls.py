from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, LoginView, GetUser

router = DefaultRouter()
router.register(r'registration', viewset=RegisterViewSet, basename='user')
router.register(r'login', viewset=LoginView, basename='user')
router.register(r'user', viewset=GetUser, basename='user')

urlpatterns = router.urls
