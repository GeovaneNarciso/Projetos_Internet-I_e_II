# Generated by Django 2.2.6 on 2019-10-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, default='', max_length=200)),
                ('balance', models.FloatField()),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('owner',),
            },
        ),
    ]
