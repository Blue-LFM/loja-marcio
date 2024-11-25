from django.contrib import admin
from django.urls import path
from projeto.settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static
from aplicacao.views import index, index2, index3, index4, index5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('1', index2),
    path('2', index3),
    path('3', index4),
    path('4', index5),
]


if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
