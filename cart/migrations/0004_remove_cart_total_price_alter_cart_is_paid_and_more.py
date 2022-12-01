# Generated by Django 4.0.4 on 2022-11-30 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('cart', '0003_alter_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='cart',
            name='is_paid',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
    ]