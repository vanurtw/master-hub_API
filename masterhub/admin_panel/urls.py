from rest_framework.urls import path
from . import views
from django.urls import include

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('profile', views.ProfileAPIViewSet, basename='admin-panel_profile')
router.register('specialist', views.SpecialistAPIViewSet, basename='admin-panel_specialist')

urlpatterns = [
    path('', include(router.urls)),

]
