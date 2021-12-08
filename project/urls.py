from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import debug_toolbar

urlpatterns = [
    path(getattr(settings, 'ADMIN_PATH', None), admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/', include('project.task_tmob.urls', 'tmob'))
]
