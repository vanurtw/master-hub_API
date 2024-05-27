from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('test', views.UsersViewSet, basename='test')



urlpatterns = [
    path('users/', views.UsersAPIView.as_view(), name='users'),
    path('s/', include(router.urls))


]
