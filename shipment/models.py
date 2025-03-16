from django.db import models

class ShipmentStatusEnum(models.TextChoices):
    PENDING = 'pending',
    SHIPPED = 'shipped',
    DELIVERED = 'delivered',

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sm_customers'

class ShipmentDestination(models.Model):
    address = models.TextField()
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sm_shipment_destinations'

class Shipment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipment_destination =models.ForeignKey(ShipmentDestination, on_delete=models.CASCADE)

    tracking_number = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(decimal_places=2, max_digits=10)
    price_est = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=10, choices=ShipmentStatusEnum.choices,
                              default=ShipmentStatusEnum.PENDING)
    note = models.TextField(blank=True)
    expected_delivery_at = models.DateTimeField(db_comment="Expected delivery date")
    arrived_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sm_shipments'

class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    qty = models.PositiveIntegerField()
    price_est = models.DecimalField(decimal_places=2, max_digits=10, db_comment="Estimate Price")
    weight = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sm_shipment_items'