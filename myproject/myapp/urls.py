
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet


router = DefaultRouter()
router.register(r'registration', viewset=RegisterViewSet, basename='user')
urlpatterns = router.urls

"""""
urlpatterns = [

    path('registration/', RegisterView.as_view())
    #  path('login/', LoginView.as_view())
    #  view.reverse_action('RegisterView', args=['1'])

]
"""""