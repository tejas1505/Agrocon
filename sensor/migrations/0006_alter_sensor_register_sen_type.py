# Generated by Django 4.0.3 on 2022-05-31 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0005_alter_sensor_register_value_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor_register',
            name='sen_type',
            field=models.CharField(max_length=20),
        ),
    ]
