from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.ServiceAPIView.as_view()),
]
