from django.urls import path, include
from rest_framework import routers

from .apps import TaskTmobConfig
from .views import RedirectViewSet

app_name = TaskTmobConfig.name

router = routers.SimpleRouter()
router.register(r'', RedirectViewSet, 'tmob-redirect-test')

urlpatterns = [
    path('', include(router.urls)),
]
