# Generated by Django 2.2 on 2019-05-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_membership_inviter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amigos', models.ManyToManyField(related_name='_perfil_amigos_+', to='myapp.Perfil')),
            ],
        ),
    ]
