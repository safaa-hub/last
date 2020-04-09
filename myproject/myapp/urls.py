from .views import RegisterView
from django.urls import path
urlpatterns = [

    path('registration/', RegisterView.as_view())

]
