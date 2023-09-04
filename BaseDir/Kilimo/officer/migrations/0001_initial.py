# Generated by Django 3.2 on 2023-08-25 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0002_auto_20230825_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='officer_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('usergroup', models.CharField(default='Officer', max_length=50)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officer', to='register.customuser')),
            ],
        ),
    ]
