from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersAPIView.as_view(), name='users')

]
