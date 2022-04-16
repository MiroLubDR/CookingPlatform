from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static

from djangoProject1.web.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',HomeView.as_view(),name='Home'),

    path('youcook/',include('djangoProject1.web.urls')),
    path('accounts/',include('djangoProject1.accounts.urls')),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)+ \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
