# Generated by Django 4.0.4 on 2022-11-19 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_rename_payment_cartitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='final_price',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]