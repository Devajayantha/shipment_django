from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="shipment_list"),
    path("create/", views.create, name="shipment_create"),
]