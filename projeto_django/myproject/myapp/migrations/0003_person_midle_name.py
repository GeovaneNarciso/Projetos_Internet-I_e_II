# Generated by Django 2.2 on 2019-04-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_person_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='midle_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]