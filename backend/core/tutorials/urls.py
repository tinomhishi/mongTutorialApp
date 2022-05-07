from django.urls import path, include
from rest_framework import routers

from tutorials.views import TutorialViewSet

router = routers.DefaultRouter()
router.register(r'tutorial', TutorialViewSet, basename='tutorial')

urlpatterns = [
    path('', include(router.urls)),
]
