# Generated by Django 5.0.7 on 2024-07-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_remove_avltest_city_ordermodel_date_ordermodel_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
