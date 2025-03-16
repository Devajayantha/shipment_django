from django.urls import path

from . import views

urlpatterns = [
    path("", views.shipment_index, name="shipment_list"),
    path("create/", views.shipment_create, name="shipment_create"),
    path("<int:id>/", views.shipment_update, name="shipment_update"),
]