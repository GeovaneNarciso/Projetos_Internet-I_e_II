# Generated by Django 2.2 on 2019-06-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_data_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]