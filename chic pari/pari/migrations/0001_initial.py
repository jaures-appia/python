# Generated by Django 2.2.3 on 2019-08-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=11)),
                ('mdp', models.CharField(max_length=100)),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
