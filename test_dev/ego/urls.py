from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'modelos', views.ModeloView, 'modelos')
router.register(r'fichas', views.FichaView, 'fichas')
router.register(r'componentes', views.ComponenteView, 'componentes')


urlpatterns = [
    # path("", views.index, name="index"),
    path('api/', include(router.urls)),
]