# Generated by Django 3.2 on 2023-08-25 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('officer', '0001_initial'),
        ('register', '0002_auto_20230825_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commented_at', models.DateTimeField(auto_now_add=True)),
                ('commented_updated', models.DateTimeField(auto_now=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('replied_at', models.DateTimeField(auto_now_add=True)),
                ('replied_updated', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main.comment')),
                ('replied_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.officerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='post_media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReplyLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('liked_updated', models.DateTimeField(auto_now=True)),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.customuser')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='main.commentreply')),
            ],
        ),
        migrations.CreateModel(
            name='RawPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.customuser')),
                ('media', models.ManyToManyField(blank=True, to='main.PostMedia')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('liked_updated', models.DateTimeField(auto_now=True)),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.customuser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='main.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='media',
            field=models.ManyToManyField(blank=True, to='main.PostMedia'),
        ),
        migrations.AddField(
            model_name='post',
            name='raw_post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='main.rawpost'),
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('liked_updated', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='main.comment')),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.customuser')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.post'),
        ),
    ]
