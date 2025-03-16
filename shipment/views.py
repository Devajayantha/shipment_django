from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from shipment.forms.shipment_form import ShipmentForm
from shipment.forms.shipment_update_form import ShipmentUpdateForm
from shipment.models import Shipment

def shipment_index(request):
    return render(request, 'index.html', context={})

def shipment_create(request: HttpRequest):
    if (request.method == "POST"):
        form = ShipmentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('shipment_list')
    else:
        form = ShipmentForm()

    return render(request, 'create.html', {"form": form})

def shipment_update(request: HttpRequest, id: int):
    shipment = (Shipment.objects
                .select_related("customer", "shipment_destination")
                .prefetch_related("shipment_items").get(id=id))

    form = ShipmentUpdateForm(request.POST or None, instance=shipment)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("shipment_list")

    return render(request, 'update.html', {'form':form, 'shipment': shipment})
