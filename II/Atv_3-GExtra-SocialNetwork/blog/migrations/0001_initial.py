# Generated by Django 2.2.6 on 2019-11-08 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('suite', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='blog.Address')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.Profile')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
