from rest_framework.routers import DefaultRouter
from .views.login_view import LoginView
from .views.register_view import RegisterViewSet
from .views.get_user_view import GetUser

router = DefaultRouter()
router.register(r'registration', viewset=RegisterViewSet, basename='user')
router.register(r'login', viewset=LoginView, basename='user')
router.register(r'user', viewset=GetUser, basename='user')

urlpatterns = router.urls
