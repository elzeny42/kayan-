# Generated by Django 5.1.7

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_vehiclemovement_operation_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasury',
            name='related_client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treasury_movements', to='accounts.client'),
        ),
    ]