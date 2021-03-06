# Generated by Django 2.0.3 on 2018-04-08 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.TextField()),
                ('picture', models.ImageField(null=True, upload_to='pictures/')),
                ('picture_url', models.TextField(null=True)),
                ('video', models.FileField(null=True, upload_to='videos/')),
                ('video_url', models.TextField(null=True)),
                ('like', models.IntegerField(null=True)),
                ('rating', models.IntegerField(null=True)),
                ('star_color', models.CharField(max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.TextField(null=True)),
                ('avatar', models.ImageField(null=True, upload_to='avatars/')),
                ('avatar_url', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Reporter'),
        ),
    ]
