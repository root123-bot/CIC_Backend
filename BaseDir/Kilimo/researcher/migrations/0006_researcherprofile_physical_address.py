# Generated by Django 3.2 on 2023-09-01 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researcher', '0005_auto_20230901_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcherprofile',
            name='physical_address',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
