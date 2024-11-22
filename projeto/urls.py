from django.contrib import admin
from django.urls import path
from projeto.settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static
from aplicacao.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]


if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)