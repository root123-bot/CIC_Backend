# Generated by Django 3.2 on 2023-08-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researcher', '0003_auto_20230827_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcherprofile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
