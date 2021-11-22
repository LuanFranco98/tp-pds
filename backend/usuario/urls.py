from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static

from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSet)
router.register('post', PostViewSet)

urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls