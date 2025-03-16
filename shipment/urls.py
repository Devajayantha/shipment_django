from django.urls import path

from . import views

urlpatterns = [
    path("", views.shipment_index, name="shipment_list"),
    path("create/", views.shipment_create, name="shipment_create"),
    path("store/", views.shipment_store, name="shipment_store"),
]