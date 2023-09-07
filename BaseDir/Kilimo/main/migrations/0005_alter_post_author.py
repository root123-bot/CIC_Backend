# Generated by Django 3.2 on 2023-09-06 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0006_officerprofile_physical_address'),
        ('main', '0004_alter_rawpost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officerposts', to='officer.officerprofile'),
        ),
    ]