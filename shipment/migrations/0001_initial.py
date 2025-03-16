# Generated by Django 5.1.7 on 2025-03-16 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'sm_customers',
            },
        ),
        migrations.CreateModel(
            name='ShipmentDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'sm_shipment_destinations',
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=50, unique=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_est', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=10)),
                ('note', models.TextField(blank=True)),
                ('expected_delivery_at', models.DateTimeField(db_comment='Expected delivery date')),
                ('arrived_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.customer')),
                ('shipment_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.shipmentdestination')),
            ],
            options={
                'db_table': 'sm_shipments',
            },
        ),
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('qty', models.PositiveIntegerField()),
                ('price_est', models.DecimalField(db_comment='Estimate Price', decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.shipment')),
            ],
            options={
                'db_table': 'sm_shipment_items',
            },
        ),
    ]
