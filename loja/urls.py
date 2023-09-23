
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static
from home.views import index

urlpatterns = [
    path('', include('produto.urls')),
    path('perfil/', include('perfil.urls')),
    path('pedido/', include('pedido.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
