# Generated by Django 3.2 on 2023-08-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officerprofile',
            name='usergroup',
            field=models.CharField(default='officer', max_length=50),
        ),
    ]
