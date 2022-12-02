# Generated by Django 4.0.4 on 2022-12-01 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_alter_cart_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cart',
            name='payment',
            field=models.CharField(choices=[('نقدی', 'cash'), ('آنلاین', 'online'), ('کیف پول', 'wallet')], default='آنلاین', help_text='choose one of the method for payment!', max_length=10),
        ),
    ]