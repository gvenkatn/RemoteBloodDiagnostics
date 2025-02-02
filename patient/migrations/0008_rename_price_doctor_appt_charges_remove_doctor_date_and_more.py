# Generated by Django 5.0.7 on 2024-07-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='price',
            new_name='appt_charges',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='date',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='items',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='is_doctor_consulation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
