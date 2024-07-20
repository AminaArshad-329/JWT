from django.urls import path
from .views import HelloView
from .api import RegisterApi

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('api/register/', RegisterApi.as_view(),name='register',)
]