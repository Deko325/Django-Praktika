# Generated by Django 4.2 on 2023-04-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='category',
            field=models.ManyToManyField(to='vetsite.category'),
        ),
    ]