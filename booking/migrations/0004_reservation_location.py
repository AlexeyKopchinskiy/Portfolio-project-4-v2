# Generated by Django 4.2.21 on 2025-05-31 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_reservation_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='booking.location'),
        ),
    ]
