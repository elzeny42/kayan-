# -*- coding: utf-8 -*-
from django.db import migrations, models

class Migration(migrations.Migration):
    """
    إضافة فهارس للحقول المستخدمة بكثرة في البحث لتحسين الأداء
    """
    
    dependencies = [
        ('accounts', '0016_treasury_related_client'),
    ]
    
    operations = [
        # إضافة فهارس لنموذج VehicleMovement
        migrations.AddIndex(
            model_name='vehiclemovement',
            index=models.Index(fields=['date'], name='vm_date_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemovement',
            index=models.Index(fields=['client'], name='vm_client_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemovement',
            index=models.Index(fields=['driver'], name='vm_driver_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemovement',
            index=models.Index(fields=['oil_type'], name='vm_oil_type_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemovement',
            index=models.Index(fields=['vehicle_number'], name='vm_vehicle_number_idx'),
        ),
        migrations.AddIndex(
            model_name='vehiclemovement',
            index=models.Index(fields=['movement_type'], name='vm_movement_type_idx'),
        ),
        
        # إضافة فهارس لنموذج Sale
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['date'], name='sale_date_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['client'], name='sale_client_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['driver'], name='sale_driver_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['oil_type'], name='sale_oil_type_idx'),
        ),
        
        # إضافة فهارس لنموذج Purchase
        migrations.AddIndex(
            model_name='purchase',
            index=models.Index(fields=['date'], name='purchase_date_idx'),
        ),
        migrations.AddIndex(
            model_name='purchase',
            index=models.Index(fields=['supplier'], name='purchase_supplier_idx'),
        ),
        migrations.AddIndex(
            model_name='purchase',
            index=models.Index(fields=['oil_type'], name='purchase_oil_type_idx'),
        ),
        
        # إضافة فهارس لنموذج Treasury
        migrations.AddIndex(
            model_name='treasury',
            index=models.Index(fields=['date'], name='treasury_date_idx'),
        ),
        migrations.AddIndex(
            model_name='treasury',
            index=models.Index(fields=['transaction_type'], name='treasury_trans_type_idx'),
        ),
        migrations.AddIndex(
            model_name='treasury',
            index=models.Index(fields=['related_client'], name='treasury_client_idx'),
        ),
        migrations.AddIndex(
            model_name='treasury',
            index=models.Index(fields=['related_driver'], name='treasury_driver_idx'),
        ),
    ]