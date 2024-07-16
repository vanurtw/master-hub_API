from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('admin-panel/profile', views.ProfileAdminViewSet, basename='admin_panel_profile')
router.register('admin-panel/specialists', views.SpecialistsAdminViewSet, basename='admin_panel_specialists')
router.register('admin-panel/services', views.ServicesAdminViewSet, basename='admin_panel_services')
router.register('admin-panel/work-time', views.WorkTimeViewSet, basename='admin_panel_worktime')
router.register('admin-panel/reviews', views.ReviewsViewSet, basename='admin-panel_reviews')

urlpatterns = [
    path('', include(router.urls)),

]
