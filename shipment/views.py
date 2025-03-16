from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from shipment.forms.shipment_form import ShipmentForm


def shipment_index(request):
    return render(request, 'index.html', context={})

def shipment_create(request):
    return render(request, 'create.html', context={})

def shipment_store(request: HttpRequest):
    if (request.method == "POST"):
        form = ShipmentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('shipment_list')
    else:
        form = ShipmentForm()

    return render(request, 'create.html', {"form": form})