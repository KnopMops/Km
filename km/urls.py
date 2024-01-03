from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static


def redirect_to_welcome(request):
    return redirect('home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_welcome, name='redirect_to_welcome'),
    path('api/v1/', include('core.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/management/', include('project.urls')),
    path('api/v1/projects/<uuid:project_id>/', include('todolist.urls')),
    path('api/v1/projects/<uuid:project_id>/<uuid:todolist_id>/', include('task.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)