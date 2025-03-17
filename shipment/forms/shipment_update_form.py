from datetime import datetime

from django import forms

from shipment.models import Shipment, ShipmentStatusEnum

class ShipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["status"]

    status = forms.ChoiceField(
        choices=ShipmentStatusEnum.choices,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    def save(self, commit=True):
        shipment = super().save(commit=False)
        shipment.status = self.cleaned_data["status"]

        if (self.cleaned_data["status"] == ShipmentStatusEnum.DELIVERED.value):
            shipment.arrived_at = datetime.now()

        if commit:
            shipment.save()

        return shipment