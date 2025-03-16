from django import forms
from django.db import transaction

from shipment.models import Shipment, Customer, ShipmentDestination, ShipmentItem
from shipment.utils.helper import generate_tracking_number


class ShipmentForm(forms.Form):
    customer_name = forms.CharField(max_length=100, required=True)
    customer_email = forms.EmailField(max_length=100, required=True)
    customer_address = forms.CharField(max_length=100, required=True)
    customer_phone = forms.CharField(max_length=50, required=True)

    address =forms.CharField(max_length=100, required=True)
    district = forms.CharField(max_length=50, required=True)
    city = forms.CharField(max_length=50, required=True)
    postal_code = forms.CharField(max_length=20, required=True)

    product_name = forms.CharField(max_length=100, required=True)
    product_price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    product_qty = forms.IntegerField(required=True)
    product_weight = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    expected_delivery_at = forms.DateTimeField(required=True)
    note = forms.CharField(widget=forms.Textarea, required=False)


    class Meta:
        model = Shipment
        fields = [
            'customer_name', 'customer_email', 'customer_address', 'customer_phone',
            'address', 'district', 'city', 'postal_code',
            'product_name', 'product_price', 'product_qty', 'product_weight', 'expected_delivery_at', 'note'
        ]


    def save(self, commit=True):
        # transaction all tables
        with transaction.atomic():
            customer = Customer.objects.create(
                name=self.cleaned_data['customer_name'],
                email=self.cleaned_data["customer_email"],
                address=self.cleaned_data["customer_address"],
                phone=self.cleaned_data["customer_phone"],
            )

            destination = ShipmentDestination.objects.create(
                address=self.cleaned_data["address"],
                district=self.cleaned_data["district"],
                city=self.cleaned_data["city"],
                postal_code=self.cleaned_data["postal_code"],
            )

            shipment = Shipment.objects.create(
                customer=customer,
                shipment_destination=destination,
                tracking_number=generate_tracking_number(),
                price_est=self.cleaned_data["product_price"],
                qty=self.cleaned_data["product_qty"],
                weight=self.cleaned_data["product_weight"],
                expected_delivery_at=self.cleaned_data["expected_delivery_at"],
                note=self.cleaned_data["note"],
            )

            if commit:
                shipment.save()

            shipment_detail = ShipmentItem.objects.create(
                shipment=shipment,
                name=self.cleaned_data["product_name"],
                price_est=self.cleaned_data["product_price"],
                qty=self.cleaned_data["product_qty"],
                weight=self.cleaned_data["product_weight"],
            )

            if commit:
                shipment_detail.save()

        return shipment
