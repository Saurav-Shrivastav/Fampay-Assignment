from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

app_name = "app"
router = DefaultRouter()
router.register("", views.VideoViewSet)


urlpatterns = [
    path("video/", include(router.urls)),
]
