from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feed.views import UserProfileViewSet, ContentViewSet, UserInteractionViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'user-interactions', UserInteractionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]