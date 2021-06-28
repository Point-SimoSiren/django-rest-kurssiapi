from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"opettajat", views.OpettajaViewSet, "nimi")
router.register(r"kurssit", views.KurssiViewSet, "id")

urlpatterns = [
    path("", include((router.urls, "app"))),
]
