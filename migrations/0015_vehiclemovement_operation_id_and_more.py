# Generated by Django 5.1.7 on 2025-03-19 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_purchase_options_alter_sale_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclemovement',
            name='operation_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='رقم العملية'),
        ),
        migrations.AddField(
            model_name='vehiclemovement',
            name='operation_type',
            field=models.CharField(blank=True, choices=[('sale', 'مبيعات'), ('purchase', 'مشتريات')], max_length=10, null=True, verbose_name='نوع العملية'),
        ),
    ]
