from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.api import views


router = DefaultRouter()
router.register("publications", views.PublicationViewSet)


urlpatterns = [path("", include(router.urls))]