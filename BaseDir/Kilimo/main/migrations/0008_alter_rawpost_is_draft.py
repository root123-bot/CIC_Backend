# Generated by Django 3.2 on 2023-09-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rawpost_saved_draft_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawpost',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
