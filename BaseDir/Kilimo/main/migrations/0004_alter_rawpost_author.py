# Generated by Django 3.2 on 2023-09-02 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_customuser_email'),
        ('main', '0003_auto_20230902_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='register.customuser'),
        ),
    ]